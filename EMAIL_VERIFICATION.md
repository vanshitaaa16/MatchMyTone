# Email Verification System - MatchMyTone

This document explains the complete email verification implementation in the MatchMyTone project.

## Overview

The email verification system ensures that users verify their email addresses before they can log in to the application. This helps prevent fake accounts and ensures valid email addresses.

---

## Technologies Used

### Backend

1. **Flask-Mail** (`Flask-Mail==0.10.0`)
   - Library for sending emails from Flask
   - Handles SMTP connections
   - Used to send verification emails

2. **Python `secrets` module**
   - Generates cryptographically secure random tokens
   - Used to create unique verification tokens

3. **Python `urllib.parse`**
   - URL encoding/decoding for tokens
   - Ensures tokens work correctly in email links

4. **PostgreSQL Database**
   - Stores verification status and tokens
   - New columns added to `users` table:
     - `email_verified` (Boolean)
     - `verification_token` (String, unique)
     - `verification_token_expires` (DateTime)

### Frontend

1. **React Native Modal**
   - Displays email verification prompt
   - Shows when user tries to login with unverified email

2. **Ionicons**
   - Envelope icon (size 80px, white color)
   - Visual indicator for email verification

---

## Database Schema Changes

### New Columns in `users` Table

```sql
ALTER TABLE users 
ADD COLUMN email_verified BOOLEAN DEFAULT FALSE NOT NULL,
ADD COLUMN verification_token VARCHAR(100) UNIQUE,
ADD COLUMN verification_token_expires TIMESTAMP;
```

### Model Changes (`backend/models.py`)

```python
class User(db.Model):
    # ... existing fields ...
    email_verified = db.Column(db.Boolean, default=False, nullable=False)
    verification_token = db.Column(db.String(100), unique=True, nullable=True)
    verification_token_expires = db.Column(db.DateTime, nullable=True)
```

---

## Configuration

### Backend Configuration (`backend/app.py`)

Email settings are configured using environment variables in `.env`:

```python
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', os.getenv('MAIL_USERNAME', ''))
```

### `.env` File Setup

```env
# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

**Important:** For Gmail, you need to:
1. Enable 2-Step Verification
2. Generate an App Password (not your regular password)
3. Use the 16-character App Password in `MAIL_PASSWORD`

---

## How It Works

### 1. User Registration

When a user registers:

1. **Token Generation** (`generate_verification_token()`)
   - Creates a 32-character random token
   - Uses `secrets.choice()` for security
   - Format: alphanumeric characters

2. **Database Storage**
   - `email_verified = False`
   - `verification_token = generated_token`
   - `verification_token_expires = current_time + 7 days`

3. **Email Sending** (`send_verification_email()`)
   - Creates HTML email with verification link
   - Link format: `http://YOUR_IP:5000/api/auth/verify-email?token=ENCODED_TOKEN`
   - Token is URL-encoded for safety

4. **Response**
   - Returns success message
   - User cannot login until email is verified

### 2. Email Verification

When user clicks the link in email:

1. **Token Extraction**
   - Extracts token from URL query parameter
   - URL-decodes the token (handles browser encoding)

2. **Token Matching**
   - Searches database for matching token
   - Handles multiple encoding variations
   - Checks token expiry

3. **Verification**
   - Sets `email_verified = True`
   - Clears `verification_token` and `verification_token_expires`
   - Returns HTML success page

4. **Error Handling**
   - Invalid token → Shows error page
   - Expired token → Shows expiry message
   - Already verified → Shows confirmation

### 3. Login Process

When user tries to login:

1. **Credentials Check**
   - Validates username and password

2. **Email Verification Check**
   - If `email_verified = False`:
     - Returns 403 error
     - Includes `user_id` and message
     - Frontend shows verification modal

3. **Success**
   - If verified, creates JWT token
   - Returns user data and token

### 4. Resend Verification

If user needs a new email:

1. **Request** (`/api/auth/resend-verification`)
   - Accepts `email` or `user_id`
   - Generates new token
   - Sends new email
   - Updates expiry time

2. **Response**
   - Success message
   - Email sent confirmation

---

## API Endpoints

### 1. Register (Modified)
**Endpoint:** `POST /api/auth/register`

**Request:**
```json
{
  "name": "username",
  "email": "user@example.com",
  "phone": "1234567890",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "User registered successfully. Please check your email to verify your account.",
  "user": { ... },
  "email_sent": true
}
```

### 2. Login (Modified)
**Endpoint:** `POST /api/auth/login`

**Request:**
```json
{
  "name": "username",
  "password": "password123"
}
```

**Response (if email not verified):**
```json
{
  "error": "Email not verified",
  "message": "Please verify your email address before logging in...",
  "email_verified": false,
  "user_id": 123
}
```

**Response (if verified):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 123,
    "name": "username",
    "email": "user@example.com",
    "token": "jwt_token_here"
  }
}
```

### 3. Verify Email
**Endpoint:** `GET /api/auth/verify-email?token=TOKEN`

**Response:**
- Returns HTML page (not JSON)
- Success: Shows confirmation page
- Error: Shows error message

### 4. Resend Verification
**Endpoint:** `POST /api/auth/resend-verification`

**Request:**
```json
{
  "email": "user@example.com",
  "user_id": 123
}
```

**Response:**
```json
{
  "message": "Verification email sent successfully",
  "email_sent": true
}
```

---

## Frontend Implementation

### Email Verification Modal (`app/index.js`)

**State Variables:**
- `showEmailVerification` - Controls modal visibility
- `verificationMessage` - Message to display
- `verificationEmail` - User's email address
- `verificationUserId` - User ID for resend

**Features:**
- Large white envelope icon (80px)
- Clear instructions
- Resend button
- Back to login button

### API Integration (`src/api.js`)

**Functions:**
1. `verifyEmail(token)` - Calls verification endpoint
2. `resendVerification(email, userId)` - Resends email

**Login Error Handling:**
- Catches "Email not verified" error
- Extracts `user_id` from error response
- Shows verification modal automatically

---

## Email Template

The verification email includes:

1. **HTML Format**
   - Professional styling
   - Responsive design
   - Brand colors

2. **Content**
   - Welcome message
   - Verification button
   - Fallback link (if button doesn't work)
   - Security notice

3. **Verification Link**
   - Format: `http://YOUR_IP:5000/api/auth/verify-email?token=TOKEN`
   - Token is URL-encoded
   - Expires in 7 days

---

## HTML Response Pages

All verification pages use a clean, minimal design:

- **Background:** Light gray (#f5f5f5)
- **Container:** White with subtle shadow
- **Icon:** Envelope emoji (📧) - 80px
- **Text:** Dark gray (#333 for headings, #666 for body)
- **No buttons** - Just information

**Pages:**
1. Success - Email verified
2. Already Verified - User already verified
3. Invalid Token - Token not found
4. Expired Token - Token expired
5. Error - General error

---

## Security Features

1. **Secure Token Generation**
   - Uses `secrets` module (cryptographically secure)
   - 32-character random tokens
   - Unique per user

2. **Token Expiry**
   - Tokens expire after 7 days
   - Prevents old links from working

3. **One-Time Use**
   - Token cleared after verification
   - Cannot be reused

4. **URL Encoding**
   - Tokens properly encoded/decoded
   - Handles special characters safely

---

## File Structure

```
MatchMyTone/
├── backend/
│   ├── app.py              # Main Flask app with email routes
│   ├── models.py           # User model with verification fields
│   ├── requirements.txt    # Includes Flask-Mail
│   └── .env                # Email configuration
├── app/
│   └── index.js            # Login modal with verification UI
└── src/
    └── api.js              # API calls for verification
```

---

## Testing

### Test Registration
1. Register a new user
2. Check email inbox
3. Click verification link
4. Should see success page

### Test Login (Unverified)
1. Try to login with unverified account
2. Should see verification modal
3. Cannot proceed until verified

### Test Resend
1. Click "Resend Verification Email"
2. Check inbox for new email
3. New token should work

---

## Troubleshooting

### Email Not Sending
- Check `.env` file configuration
- Verify Gmail App Password (not regular password)
- Ensure 2-Step Verification is enabled
- Check backend logs for errors

### Token Not Working
- Check if token expired (7 days)
- Verify token encoding/decoding
- Check database for correct token
- Look at backend logs for matching attempts

### Modal Not Showing
- Check `src/api.js` error handling
- Verify login response includes `user_id`
- Check React Native console for errors

---

## Summary

The email verification system uses:
- **Flask-Mail** for sending emails
- **Secure token generation** with Python secrets
- **Database fields** to track verification status
- **HTML email templates** for professional emails
- **React Native modals** for user interaction
- **Clean HTML pages** for verification responses

All components work together to ensure users verify their email addresses before accessing the application.


