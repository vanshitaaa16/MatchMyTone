# MatchMyTone Backend API

Flask backend with PostgreSQL for the MatchMyTone application.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up PostgreSQL Database

1. Install PostgreSQL if not already installed
2. Create a database:
```sql
CREATE DATABASE matchmytone;
```

3. Update `.env` file with your database credentials:
```
DATABASE_URL=postgresql://username:password@localhost:5432/matchmytone
```

### 3. Create .env File

Copy `.env.example` to `.env` and update with your configuration:
```bash
cp .env.example .env
```

### 4. Run the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user

### Profile

- `GET /api/users/profile` - Get user profile (requires JWT token)
- `PUT /api/users/profile` - Update user profile (requires JWT token)

### Quiz Results

- `POST /api/quiz/skincare` - Save skincare analysis result (requires JWT token)
- `POST /api/quiz/body-shape` - Save body shape analysis result (requires JWT token)
- `POST /api/quiz/face-shape` - Save face shape analysis result (requires JWT token)
- `GET /api/quiz/results` - Get all quiz results for user (requires JWT token)
- `GET /api/quiz/<quiz_type>` - Get specific quiz result (requires JWT token)

### Health Check

- `GET /api/health` - Check API status

## Authentication

All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

The token is returned upon successful login/registration and expires after 30 days.

## Database Schema

### Users Table
- id (Integer, Primary Key)
- name (String, Unique)
- email (String, Unique)
- phone (String, Unique)
- password (String, Hashed)
- gender (String)
- dob (String)
- age (Integer)
- created_at (DateTime)
- updated_at (DateTime)

### Quiz Results Table
- id (Integer, Primary Key)
- user_id (Integer, Foreign Key)
- quiz_type (String: 'skincare', 'body_shape', 'face_shape')
- answers (JSON)
- result (String)
- created_at (DateTime)
- updated_at (DateTime)






















