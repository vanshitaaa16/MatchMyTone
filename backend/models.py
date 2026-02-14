from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with quiz results
    quiz_results = db.relationship('QuizResult', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'gender': self.gender,
            'dob': self.dob,
            'age': self.age,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class QuizResult(db.Model):
    __tablename__ = 'quiz_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_type = db.Column(db.String(50), nullable=False)  # 'skincare', 'body_shape', 'face_shape'
    answers = db.Column(db.JSON, nullable=False)  # Store quiz answers as JSON
    result = db.Column(db.String(100))  # Store the calculated result
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Unique constraint: one result per quiz type per user
    __table_args__ = (db.UniqueConstraint('user_id', 'quiz_type', name='unique_user_quiz'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'quiz_type': self.quiz_type,
            'answers': self.answers,
            'result': self.result,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ColorAnalysisResult(db.Model):
    __tablename__ = 'color_analysis_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo_uri = db.Column(db.String(500))  # Store photo URI/path
    season_type = db.Column(db.String(100))
    season_description = db.Column(db.Text)
    undertone = db.Column(db.String(50))
    undertone_description = db.Column(db.Text)
    colors_to_wear = db.Column(db.JSON)  # Array of {name, hex}
    colors_to_avoid = db.Column(db.JSON)  # Array of {name, hex}
    is_face = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text)  # For non-face cases
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with user
    user = db.relationship('User', backref='color_analysis_results')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'photo_uri': self.photo_uri,
            'season_type': self.season_type,
            'season_description': self.season_description,
            'undertone': self.undertone,
            'undertone_description': self.undertone_description,
            'colors_to_wear': self.colors_to_wear,
            'colors_to_avoid': self.colors_to_avoid,
            'is_face': self.is_face,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }





















