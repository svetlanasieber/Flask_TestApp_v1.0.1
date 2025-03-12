from flask import Flask, render_template, request, jsonify
import calculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # Validate that all required data is present
        if not data or 'num1' not in data or 'num2' not in data or 'operation' not in data:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Handle possible None or invalid values
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
        
        # Format result for display (avoid too many decimal places)
        if isinstance(result, float):
            # If result is a whole number, convert to int
            if result.is_integer():
                result = int(result)
            else:
                # Limit to 8 decimal places and remove trailing zeros
                result = float(f"{result:.8f}".rstrip('0').rstrip('.') if '.' in f"{result:.8f}" else f"{result:.8f}")
        
        return jsonify({'result': result})
    
    except Exception as e:
        app.logger.error(f"Calculation error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    print("Starting Flask web server...")
    print("Open http://127.0.0.1:5000/ in your browser to use the calculator")
    app.run(debug=True) 