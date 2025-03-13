from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    settings = db.relationship('UserSettings', backref='user', uselist=False, cascade="all, delete-orphan")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    theme = db.Column(db.String(20), default='standard')  
    decimal_places = db.Column(db.Integer, default=2)
    scientific_notation = db.Column(db.Boolean, default=False)
    calculation_history = db.Column(db.Text, default='[]')  
    
    def add_calculation(self, calculation):
        """Add a calculation to the history"""
        history = json.loads(self.calculation_history)
        history.append({
            'calculation': calculation,
            'timestamp': datetime.utcnow().isoformat()
        })
        
      
        if len(history) > 100:
            history = history[-100:]
        
        self.calculation_history = json.dumps(history)
    
    def get_history(self):
        """Get the calculation history as a Python list"""
        return json.loads(self.calculation_history)
    
    def __repr__(self):
        return f'<UserSettings for {self.user.username}>' 
