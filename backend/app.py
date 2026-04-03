from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
import os
import uuid
import resend
from dotenv import load_dotenv
from models import db, User, QuizResult, ColorAnalysisResult
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

load_dotenv()

# Configure Resend
resend.api_key = (os.getenv('RESEND_API_KEY', '') or '').strip()
FROM_EMAIL = (os.getenv('FROM_EMAIL', 'MatchMyTone <noreply@matchmytone.online>') or '').strip()
# Used to build the verification link sent by email.
BACKEND_URL = (os.getenv('BACKEND_URL', 'https://matchmytone.onrender.com') or '').strip().rstrip('/')

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

# Create tables (safe for production — handles existing tables)
with app.app_context():
    try:
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()
        
        if 'users' not in existing_tables:
            db.create_all()
            print("[DB] Tables created successfully")
        else:
            # Tables exist — only create missing ones
            db.create_all()
            print("[DB] Tables verified (existing tables preserved)")
    except Exception as e:
        print(f"[DB] create_all handled gracefully: {e}")
    
    # Lightweight schema safety: add new columns if DB already has older table.
    try:
        db.session.execute(text("ALTER TABLE color_analysis_results ADD COLUMN IF NOT EXISTS skin_age INTEGER;"))
        db.session.execute(text("ALTER TABLE color_analysis_results ADD COLUMN IF NOT EXISTS skin_age_description TEXT;"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print("[DB] Warning: could not auto-migrate color_analysis_results skin_age columns:", e)
    
    # Add email verification columns if missing
    try:
        db.session.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_verified BOOLEAN DEFAULT FALSE;"))
        db.session.execute(text("ALTER TABLE users ADD COLUMN IF NOT EXISTS verification_token VARCHAR(100);"))
        db.session.commit()
        print("[DB] Email verification columns ensured")
    except Exception as e:
        db.session.rollback()
        print("[DB] Warning: could not auto-migrate email verification columns:", e)

    # Drop unique constraint so multiple results per user per quiz type can be stored
    try:
        db.session.execute(text("ALTER TABLE quiz_results DROP CONSTRAINT IF EXISTS unique_user_quiz;"))
        db.session.commit()
        print("[DB] Dropped unique_user_quiz constraint (if it existed)")
    except Exception as e:
        db.session.rollback()
        print("[DB] Warning: could not drop unique_user_quiz constraint:", e)
    
    # Close the master process's DB connection pool so that forked gunicorn
    # workers each create their own fresh SSL connections to PostgreSQL.
    db.engine.dispose()
    print("[DB] Connection pool disposed (workers will create fresh connections)")


# ==================== EMAIL HELPER ====================

def generate_verification_token():
    """Generate a unique verification token."""
    return uuid.uuid4().hex

def send_verification_email(email, token):
    """Send a verification link email via Resend."""
    try:
        verify_url = f"{BACKEND_URL}/api/auth/verify-email?token={token}"
        params = {
            "from": FROM_EMAIL,
            "to": [email],
            "subject": "Verify your MatchMyTone account",
            "html": f"""
            <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 480px; margin: 0 auto; padding: 32px; background: #FFF8E7; border-radius: 16px;">
                <h1 style="color: #2C2C2C; font-size: 24px; text-align: center; margin-bottom: 8px;">MatchMyTone</h1>
                <p style="color: #6B6B6B; text-align: center; font-size: 14px; margin-bottom: 24px;">Verify your email address</p>
                <div style="background: #FFFFFF; border-radius: 12px; padding: 24px; text-align: center; border: 1px solid #EAD9A1;">
                    <p style="color: #4F4F4F; font-size: 14px; margin-bottom: 20px;">Click the button below to verify your email and activate your account:</p>
                    <a href="{verify_url}" style="display: inline-block; padding: 14px 32px; background: #C24C4A; color: #FFFFFF; text-decoration: none; border-radius: 10px; font-weight: 700; font-size: 16px;">Verify My Email</a>
                    <p style="color: #8A7F70; font-size: 12px; margin-top: 20px;">Or copy and paste this link in your browser:</p>
                    <p style="color: #A46B39; font-size: 11px; word-break: break-all;">{verify_url}</p>
                </div>
                <p style="color: #A46B39; text-align: center; font-size: 12px; margin-top: 20px;">If you didn't create an account, you can safely ignore this email.</p>
            </div>
            """
        }
        email_response = resend.Emails.send(params)
        print(f"[EMAIL] Verification email sent to {email}: {email_response}")
        return True
    except Exception as e:
        import traceback
        print(f"[EMAIL] Error sending verification email to {email}: {e}")
        print(f"[EMAIL] Full traceback: {traceback.format_exc()}")
        print(f"[EMAIL] Resend API key set: {bool(resend.api_key)}")
        print(f"[EMAIL] From email: {FROM_EMAIL}")
        return False


# Debug endpoint — remove after testing
@app.route('/api/test-email', methods=['GET'])
def test_email():
    """Debug endpoint to test Resend configuration."""
    api_key_set = bool(resend.api_key) and len(resend.api_key) > 5
    api_key_preview = resend.api_key[:8] + '...' if api_key_set else 'NOT SET'
    
    result = {
        'resend_api_key_set': api_key_set,
        'api_key_preview': api_key_preview,
        'from_email': FROM_EMAIL,
        'backend_url': BACKEND_URL
    }
    
    # Try sending a test email if ?send=true is passed
    test_to = request.args.get('send')
    if test_to:
        try:
            params = {
                "from": FROM_EMAIL,
                "to": [test_to],
                "subject": "MatchMyTone Test Email",
                "html": "<h1>It works!</h1><p>Your Resend integration is configured correctly.</p>"
            }
            response = resend.Emails.send(params)
            result['email_sent'] = True
            result['resend_response'] = str(response)
        except Exception as e:
            result['email_sent'] = False
            result['error'] = str(e)
    
    return jsonify(result), 200

# ==================== AUTHENTICATION ENDPOINTS ====================

@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        print(f"[REGISTER] Received request from {request.remote_addr}")
        data = request.get_json()
        print(f"[REGISTER] Data: {data}")
        
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
        
        # Generate verification token
        token = generate_verification_token()
        
        # Create new user (unverified)
        new_user = User(
            name=data['name'],
            email=data['email'].lower(),
            phone=data['phone'],
            password=hashed_password,
            gender=data['gender'],
            dob=data['dob'],
            age=data['age'],
            is_verified=False,
            verification_token=token
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Send verification email via Resend
        email_sent = send_verification_email(new_user.email, token)
        
        user_data = {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'phone': new_user.phone,
            'gender': new_user.gender,
            'dob': new_user.dob,
            'age': new_user.age,
            'is_verified': False
        }
        
        msg = 'Registration successful! Please check your email and click the verification link.'
        if not email_sent:
            msg = 'Registration successful but could not send verification email. Please try again from the login page.'
        
        return jsonify({'message': msg, 'user': user_data, 'requires_verification': True}), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already exists'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/auth/verify-email', methods=['GET'])
def verify_email():
    """Verify user email via link click — returns an HTML success/error page."""
    token = request.args.get('token', '').strip()
    
    if not token:
        return '<h2>Invalid verification link.</h2>', 400
    
    user = User.query.filter_by(verification_token=token).first()
    
    if not user:
        return """
        <html><body style="font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #FFF8E7;">
            <div style="text-align: center; padding: 40px; background: white; border-radius: 16px; border: 1px solid #EAD9A1;">
                <h1 style="color: #C24C4A;">❌ Invalid Link</h1>
                <p style="color: #6B6B6B;">This verification link is invalid or has already been used.</p>
            </div>
        </body></html>
        """, 400
    
    if user.is_verified:
        return """
        <html><body style="font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #FFF8E7;">
            <div style="text-align: center; padding: 40px; background: white; border-radius: 16px; border: 1px solid #EAD9A1;">
                <h1 style="color: #2C2C2C;">✅ Already Verified</h1>
                <p style="color: #6B6B6B;">Your email is already verified. You can log in to MatchMyTone.</p>
            </div>
        </body></html>
        """, 200
    
    # Mark as verified and clear token
    user.is_verified = True
    user.verification_token = None
    db.session.commit()
    
    return f"""
    <html><body style="font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #FFF8E7;">
        <div style="text-align: center; padding: 40px; background: white; border-radius: 16px; border: 1px solid #EAD9A1;">
            <h1 style="color: #2C2C2C;">✅ Email Verified!</h1>
            <p style="color: #6B6B6B; font-size: 16px;">Welcome, <strong>{user.name}</strong>!</p>
            <p style="color: #4F4F4F;">Your email has been verified. You can now log in to MatchMyTone.</p>
        </div>
    </body></html>
    """, 200


@app.route('/api/auth/resend-verification', methods=['POST'])
def resend_verification():
    """Resend verification email with a new link."""
    try:
        data = request.get_json()
        # Frontend currently sends the login "username" here as `email`.
        # So, accept both "email" and "name" styles to prevent false "User not found".
        identity = (data.get('email') or data.get('name') or '').lower().strip()

        if not identity:
            return jsonify({'error': 'Email is required'}), 400

        # 1) Try by email
        user = User.query.filter_by(email=identity).first()

        # 2) If not found and it doesn't look like an email, try by username
        if not user and '@' not in identity:
            user = User.query.filter(User.name.ilike(identity)).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        if user.is_verified:
            return jsonify({'message': 'Email already verified. You can log in.'}), 200
        
        # Generate new token and send email
        new_token = generate_verification_token()
        user.verification_token = new_token
        db.session.commit()
        
        email_sent = send_verification_email(user.email, new_token)
        
        if email_sent:
            return jsonify({'message': 'Verification link sent to your email.'}), 200
        else:
            return jsonify({'error': 'Could not send verification email. Please try again.'}), 500
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        print(f"[LOGIN] Received request from {request.remote_addr}")
        data = request.get_json()
        
        if not data.get('name') or not data.get('password'):
            return jsonify({'error': 'Username and password are required'}), 400
        
        # Find user by name (case-insensitive)
        user = User.query.filter(User.name.ilike(data['name'])).first()
        
        if not user or not bcrypt.check_password_hash(user.password, data['password']):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        # Check if email is verified
        if not user.is_verified:
            return jsonify({
                'error': 'Please verify your email before logging in.',
                'requires_verification': True,
                'email': user.email
            }), 403
        
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
            'is_verified': True,
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
        
        # Validate required fields (email and username cannot be changed)
        if not data.get('phone') or not data.get('gender') or not data.get('dob'):
            return jsonify({'error': 'All fields are required'}), 400
        
        # Validate phone number
        if len(data['phone']) != 10:
            return jsonify({'error': 'Phone number must be exactly 10 digits'}), 400
        
        # Check for phone duplicate (excluding current user)
        if data['phone'] != user.phone:
            existing_phone = User.query.filter(User.phone == data['phone']).filter(User.id != user.id).first()
            if existing_phone:
                return jsonify({'error': 'This phone number is already registered.'}), 400
        
        # Update user data (username and email cannot be changed)
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
        
        # Always create a new result (save all attempts)
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
        
        # Always create a new result (save all attempts)
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
        
        # Always create a new result (save all attempts)
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
        
        # Get ALL quiz results grouped by type (newest first)
        all_quiz_results = QuizResult.query.filter_by(user_id=user_id).order_by(QuizResult.created_at.desc()).all()
        all_color_results = ColorAnalysisResult.query.filter_by(user_id=user_id).order_by(ColorAnalysisResult.created_at.desc()).all()
        
        # Group quiz results by type as lists
        results_data = {
            'skincare': [],
            'body_shape': [],
            'face_shape': [],
            'color_analysis': []
        }
        
        for result in all_quiz_results:
            if result.quiz_type in results_data:
                results_data[result.quiz_type].append(result.to_dict())

        for color_result in all_color_results:
            results_data['color_analysis'].append(color_result.to_dict())
        
        return jsonify({'results': results_data}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/color-analysis', methods=['POST'])
@jwt_required()
def save_color_analysis_result():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        # Allow both face and non-face results (is_face can be True or False)
        if 'is_face' not in data:
            return jsonify({'error': 'is_face field is required'}), 400
        
        # Always create a new result (save all attempts)
        new_result = ColorAnalysisResult(
            user_id=user_id,
            photo_uri=data.get('photo_uri'),
            season_type=data.get('season_type'),
            season_description=data.get('season_description'),
            undertone=data.get('undertone'),
            undertone_description=data.get('undertone_description'),
            skin_age=data.get('skin_age'),
            skin_age_description=data.get('skin_age_description'),
            colors_to_wear=data.get('colors_to_wear', []),
            colors_to_avoid=data.get('colors_to_avoid', []),
            is_face=data.get('is_face', True),
            description=data.get('description')
        )
        db.session.add(new_result)
        db.session.commit()
        return jsonify({'message': 'Color analysis result saved successfully', 'result': new_result.to_dict()}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/color-analysis/<int:result_id>', methods=['GET'])
@jwt_required()
def get_color_analysis_by_id(result_id):
    try:
        user_id = get_jwt_identity()
        result = ColorAnalysisResult.query.filter_by(id=result_id, user_id=user_id).first()
        
        if not result:
            return jsonify({'message': 'No result found', 'result': None}), 200
        
        return jsonify({'result': result.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quiz/<quiz_type>', methods=['GET'])
@jwt_required()
def get_quiz_result(quiz_type):
    try:
        user_id = get_jwt_identity()
        
        valid_types = ['skincare', 'body_shape', 'face_shape', 'color_analysis']
        if quiz_type not in valid_types:
            return jsonify({'error': 'Invalid quiz type'}), 400
        
        if quiz_type == 'color_analysis':
            # Return all color analysis results
            results = ColorAnalysisResult.query.filter_by(user_id=user_id).order_by(ColorAnalysisResult.created_at.desc()).all()
            return jsonify({'results': [r.to_dict() for r in results]}), 200
        
        # Return all results for this quiz type (newest first)
        results = QuizResult.query.filter_by(
            user_id=user_id,
            quiz_type=quiz_type
        ).order_by(QuizResult.created_at.desc()).all()
        
        if not results:
            return jsonify({'message': 'No result found', 'results': []}), 200
        
        return jsonify({'results': [r.to_dict() for r in results]}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

