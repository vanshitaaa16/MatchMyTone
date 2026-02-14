# 🚀 Quick Start Guide - MatchMyTone

## Prerequisites

1. **Python 3.8+** installed
2. **Node.js 16+** installed  
3. **PostgreSQL** installed and running
4. **Expo CLI** installed globally: `npm install -g expo-cli`

## Step 1: Install Dependencies

### Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Frontend Dependencies
```bash
npm install
```

## Step 2: Setup Database

1. **Start PostgreSQL service**

2. **Create the database:**
```sql
CREATE DATABASE matchmytone;
```

3. **Create tables:**
   - The app will auto-create tables on first run
   - Or manually run: `backend/CREATE_COLOR_ANALYSIS_TABLE.sql` if needed

4. **Configure database connection:**
   - Edit `backend/.env` (create if it doesn't exist):
   ```
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/matchmytone
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   ```

## Step 3: Start the Application

### Option A: Use the Startup Script (Easiest)
```bash
START_APP.bat
```

### Option B: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
```

**Terminal 2 - Frontend:**
```bash
npm start
# or
expo start
```

## Step 4: Test the Setup

1. **Test Backend:**
   - Open browser: `http://localhost:5000/api/health`
   - Should see: `{"status": "ok", "message": "API is running"}`

2. **Test Frontend:**
   - Scan QR code with Expo Go app (for physical device)
   - Or press `a` for Android emulator
   - Or press `i` for iOS simulator

## Troubleshooting

### Backend Issues

**Port 5000 already in use:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**Database connection error:**
- Make sure PostgreSQL is running
- Check database name and password in `.env`
- Verify database exists: `psql -U postgres -l`

**Windows Firewall blocking:**
- When starting backend, Windows may ask to allow Python through firewall
- Click "Allow access" for both Private and Public networks

### Frontend Issues

**Network request failed:**
- Make sure backend is running on port 5000
- For Android emulator: Uses `http://10.0.2.2:5000/api` (auto-configured)
- For physical device: Make sure phone and computer are on same Wi-Fi network
- Check Windows Firewall settings

**Module not found errors:**
```bash
# Clear cache and reinstall
rm -rf node_modules
npm install
npx expo start --clear
```

**Expo Go connection issues:**
- Make sure phone and computer are on same network
- Try using Expo tunnel: `npx expo start --tunnel`

## API Configuration

The app automatically detects the platform:
- **Android Emulator**: `http://10.0.2.2:5000/api`
- **iOS Simulator**: `http://localhost:5000/api`
- **Physical Device**: Uses your computer's IP (auto-detected)

To change API URL, edit `src/api.js`

## Need Help?

Run the setup checker:
```bash
CHECK_SETUP.bat
```

This will verify:
- Python installation
- Node.js installation
- Backend dependencies
- Frontend dependencies
- Database connection





