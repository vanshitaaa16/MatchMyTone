from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os
from dotenv import load_dotenv
from models import db, User, QuizResult
from sqlalchemy.exc import IntegrityError

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:postgres@localhost:5432/matchmytone'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string-change-in-production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
# Enable CORS for all routes and origins (for development)
CORS(app, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

# Create tables
with app.app_context():
    db.create_all()

# ==================== AUTHENTICATION ENDPOINTS ====================

@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'password', 'gender', 'dob', 'age']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field.capitalize()} is required'}), 400
        
        # Check if user already exists
        existing_user = User.query.filter(
            (User.email == data['email'].lower()) | 
            (User.name.ilike(data['name'])) |
            (User.phone == data['phone'])
        ).first()
        
        if existing_user:
            if existing_user.email.lower() == data['email'].lower():
                return jsonify({'error': 'Email already exists'}), 400
            elif existing_user.name.lower() == data['name'].lower():
                return jsonify({'error': 'Username already exists'}), 400
            elif existing_user.phone == data['phone']:
                return jsonify({'error': 'Phone number already exists'}), 400
        
        # Validate phone number
        if len(data['phone']) != 10:
            return jsonify({'error': 'Phone number must be exactly 10 digits'}), 400
        
        # Validate email format
        if '@' not in data['email'] or (not data['email'].endswith('.com') and not data['email'].endswith('.in')):
            return jsonify({'error': 'Email must contain @ and end with .com or .in'}), 400
        
        # Hash password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        # Create new user
        new_user = User(
            name=data['name'],
            email=data['email'].lower(),
            phone=data['phone'],
            password=hashed_password,
            gender=data['gender'],
            dob=data['dob'],
            age=data['age']
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Create access token
        access_token = create_access_token(identity=str(new_user.id))
        
        # Return user data (without password)
        user_data = {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'phone': new_user.phone,
            'gender': new_user.gender,
            'dob': new_user.dob,
            'age': new_user.age,
            'token': access_token
        }
        
        return jsonify({'message': 'Registration successful', 'user': user_data}), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already exists'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('password'):
            return jsonify({'error': 'Username and password are required'}), 400
        
        # Find user by name (case-insensitive)
        user = User.query.filter(User.name.ilike(data['name'])).first()
        
        if not user or not bcrypt.check_password_hash(user.password, data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Create access token
        access_token = create_access_token(identity=str(user.id))
        
        # Return user data (without password)
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'gender': user.gender,
            'dob': user.dob,
            'age': user.age,
            'token': access_token
        }
        
        return jsonify({'message': 'Login successful', 'user': user_data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== PROFILE ENDPOINTS ====================

@app.route('/api/users/profile', methods=['GET'])
@jwt_required()
def get_profile():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'gender': user.gender,
            'dob': user.dob,
            'age': user.age
        }
        
        return jsonify({'user': user_data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        # Validate required fields
        if not data.get('email') or not data.get('phone') or not data.get('gender') or not data.get('dob'):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Validate phone number
        if len(data['phone']) != 10:
            return jsonify({'error': 'Phone number must be exactly 10 digits'}), 400
        
        # Validate email format
        if '@' not in data['email'] or (not data['email'].endswith('.com') and not data['email'].endswith('.in')):
            return jsonify({'error': 'Email must contain @ and end with .com or .in'}), 400
        
        # Check for duplicates (excluding current user)
        if data['email'].lower() != user.email.lower():
            existing_email = User.query.filter(User.email == data['email'].lower()).filter(User.id != user.id).first()
            if existing_email:
                return jsonify({'error': 'This email address is already registered.'}), 400
        
        if data['phone'] != user.phone:
            existing_phone = User.query.filter(User.phone == data['phone']).filter(User.id != user.id).first()
            if existing_phone:
                return jsonify({'error': 'This phone number is already registered.'}), 400
        
        # Update user data (username cannot be changed)
        user.email = data['email'].lower()
        user.phone = data['phone']
        user.gender = data['gender']
        user.dob = data['dob']
        user.age = data.get('age', user.age)
        
        db.session.commit()
        
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'gender': user.gender,
            'dob': user.dob,
            'age': user.age
        }
        
        return jsonify({'message': 'Profile updated successfully', 'user': user_data}), 200
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Update failed due to duplicate data'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# ==================== QUIZ RESULT ENDPOINTS ====================

@app.route('/api/quiz/skincare', methods=['POST'])
@jwt_required()
def save_skincare_result():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('answers'):
            return jsonify({'error': 'Answers are required'}), 400
        
        # Check if result already exists for this user
        existing_result = QuizResult.query.filter_by(
            user_id=user_id,
            quiz_type='skincare'
        ).first()
        
        if existing_result:
            existing_result.answers = data['answers']
            existing_result.result = data.get('result', '')
            db.session.commit()
            return jsonify({'message': 'Skincare result updated successfully', 'result': existing_result.to_dict()}), 200
        else:
            new_result = QuizResult(
                user_id=user_id,
                quiz_type='skincare',
                answers=data['answers'],
                result=data.get('result', '')
            )
            db.session.add(new_result)
            db.session.commit()
            return jsonify({'message': 'Skincare result saved successfully', 'result': new_result.to_dict()}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/body-shape', methods=['POST'])
@jwt_required()
def save_body_shape_result():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('answers'):
            return jsonify({'error': 'Answers are required'}), 400
        
        existing_result = QuizResult.query.filter_by(
            user_id=user_id,
            quiz_type='body_shape'
        ).first()
        
        if existing_result:
            existing_result.answers = data['answers']
            existing_result.result = data.get('result', '')
            db.session.commit()
            return jsonify({'message': 'Body shape result updated successfully', 'result': existing_result.to_dict()}), 200
        else:
            new_result = QuizResult(
                user_id=user_id,
                quiz_type='body_shape',
                answers=data['answers'],
                result=data.get('result', '')
            )
            db.session.add(new_result)
            db.session.commit()
            return jsonify({'message': 'Body shape result saved successfully', 'result': new_result.to_dict()}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/face-shape', methods=['POST'])
@jwt_required()
def save_face_shape_result():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('answers'):
            return jsonify({'error': 'Answers are required'}), 400
        
        existing_result = QuizResult.query.filter_by(
            user_id=user_id,
            quiz_type='face_shape'
        ).first()
        
        if existing_result:
            existing_result.answers = data['answers']
            existing_result.result = data.get('result', '')
            db.session.commit()
            return jsonify({'message': 'Face shape result updated successfully', 'result': existing_result.to_dict()}), 200
        else:
            new_result = QuizResult(
                user_id=user_id,
                quiz_type='face_shape',
                answers=data['answers'],
                result=data.get('result', '')
            )
            db.session.add(new_result)
            db.session.commit()
            return jsonify({'message': 'Face shape result saved successfully', 'result': new_result.to_dict()}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/results', methods=['GET'])
@jwt_required()
def get_quiz_results():
    try:
        user_id = get_jwt_identity()
        
        results = QuizResult.query.filter_by(user_id=user_id).all()
        
        results_data = {
            'skincare': None,
            'body_shape': None,
            'face_shape': None
        }
        
        for result in results:
            results_data[result.quiz_type] = result.to_dict()
        
        return jsonify({'results': results_data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/<quiz_type>', methods=['GET'])
@jwt_required()
def get_quiz_result(quiz_type):
    try:
        user_id = get_jwt_identity()
        
        valid_types = ['skincare', 'body_shape', 'face_shape']
        if quiz_type not in valid_types:
            return jsonify({'error': 'Invalid quiz type'}), 400
        
        result = QuizResult.query.filter_by(
            user_id=user_id,
            quiz_type=quiz_type
        ).first()
        
        if not result:
            return jsonify({'message': 'No result found', 'result': None}), 200
        
        return jsonify({'result': result.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

