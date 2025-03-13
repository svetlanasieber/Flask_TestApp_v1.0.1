from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import calculator
import json
import os
import pymysql
from models import db, User, UserSettings
import urllib.parse


pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')


password = urllib.parse.quote_plus("kad0renk 1212")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost/calculator_db?auth_plugin=mysql_native_password'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


def create_database():
    try:
        
        engine = pymysql.connect(
            host='localhost',
            user='',
            password='',
            # Use the native password authentication plugin
            client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
        )
        cursor = engine.cursor()
        
      
        cursor.execute("CREATE DATABASE IF NOT EXISTS calculator_db")
        
       
        cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'kad0renk 1212'")
        
        cursor.close()
        engine.close()
        
      
        with app.app_context():
            db.create_all()
        print("Database and tables created successfully!")
    except Exception as e:
        print(f"Database error: {str(e)}")


@app.before_request
def check_database():
    if not hasattr(app, 'db_initialized'):
        create_database()
        app.db_initialized = True

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    theme = 'standard'
    if current_user.is_authenticated:
        theme = current_user.settings.theme
    return render_template('calculator.html', theme=theme)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
      
        if not data or 'num1' not in data or 'num2' not in data or 'operation' not in data:
            return jsonify({'error': 'Missing required parameters'}), 400
        
       
        try:
            num1 = float(data['num1']) if data['num1'] is not None else 0
            num2 = float(data['num2']) if data['num2'] is not None else 0
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid number format'}), 400
        
        operation = data['operation']
        
        result = None
        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = calculator.divide(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
      
        if isinstance(result, float):
            decimal_places = 8  # Default
            if current_user.is_authenticated:
                decimal_places = current_user.settings.decimal_places
                
          
            if (current_user.is_authenticated and 
                current_user.settings.scientific_notation and 
                (abs(result) >= 1e6 or (abs(result) < 1e-6 and result != 0))):
                result = format(result, f'.{decimal_places}e')
            else:
              
                if result.is_integer():
                    result = int(result)
                else:
                
                    result_str = f"{result:.{decimal_places}f}"
                    result = float(result_str.rstrip('0').rstrip('.') if '.' in result_str else result_str)
        
       
        if current_user.is_authenticated:
            operation_symbols = {
                'add': '+',
                'subtract': '-',
                'multiply': '×',
                'divide': '÷'
            }
            calculation_str = f"{num1} {operation_symbols[operation]} {num2} = {result}"
            current_user.settings.add_calculation(calculation_str)
            db.session.commit()
        
        return jsonify({'result': result})
    
    except Exception as e:
        app.logger.error(f"Calculation error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
       
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!')
            return redirect(url_for('register'))
            
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already registered!')
            return redirect(url_for('register'))
        
     
        user = User(username=username, email=email)
        user.set_password(password)
        
     
        settings = UserSettings(user=user)
        
        db.session.add(user)
        db.session.add(settings)
        db.session.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def user_settings():
    if request.method == 'POST':
        # Update settings
        current_user.settings.theme = request.form.get('theme')
        current_user.settings.decimal_places = int(request.form.get('decimal_places'))
        current_user.settings.scientific_notation = 'scientific_notation' in request.form
        
        db.session.commit()
        flash('Settings saved successfully!')
        
    return render_template('settings.html', settings=current_user.settings)

@app.route('/history')
@login_required
def view_history():
    history = current_user.settings.get_history()
    return render_template('history.html', history=history)

@app.route('/save_calculation', methods=['POST'])
@login_required
def save_calculation():
    data = request.get_json()
    calculation = data.get('calculation')
    
    current_user.settings.add_calculation(calculation)
    db.session.commit()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    print("Starting Flask web server...")
    print("Open http://127.0.0.1:5000/ in your browser to use the calculator")

    create_database()
    app.run(debug=True) 
