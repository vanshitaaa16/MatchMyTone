# 🚀 Complete Setup Guide - Run Your Project Successfully

## Step 1: Complete Firewall Rule Setup

You're currently on the "Name" step:

1. **Name:** Enter `Flask Backend Port 5000`
2. **Description (optional):** Enter `Allow Flask backend server on port 5000 for MatchMyTone app`
3. Click **"Finish"**

✅ The firewall rule is now created!

---

## Step 2: Start Your Backend Server

1. **Open a terminal/command prompt**
2. **Navigate to backend folder:**
   ```bash
   cd C:\Users\VANSHITA SHAH\MatchMyTone\backend
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```

4. **You should see:**
   ```
   * Serving Flask app 'app'
   * Debug mode: on
   * Running on http://0.0.0.0:5000
   * Running on http://127.0.0.1:5000
   ```

5. **Keep this terminal open** - don't close it! The backend must stay running.

✅ Backend is now running!

---

## Step 3: Test Backend is Working

1. **Open your web browser**
2. **Go to:**
   ```
   http://localhost:5000/api/health
   ```

3. **You should see:**
   ```json
   {"status": "ok", "message": "API is running"}
   ```

✅ Backend is accessible!

---

## Step 4: Start Your React Native Frontend

1. **Open a NEW terminal/command prompt** (keep the backend terminal running)
2. **Navigate to project root:**
   ```bash
   cd C:\Users\VANSHITA SHAH\MatchMyTone
   ```

3. **Start Expo:**
   ```bash
   npm start
   ```
   or
   ```bash
   expo start
   ```

4. **You should see the Expo Dev Tools** with QR code and options

✅ Frontend is starting!

---

## Step 5: Run on Android Emulator

1. **In the Expo terminal**, press `a` to run on Android emulator
2. **Or scan the QR code** with Expo Go app on your phone
3. **Wait for the app to load**

✅ App is running!

---

## Step 6: Test Registration/Login

1. **In your app**, click "Register"
2. **Fill in all fields:**
   - Name
   - Email
   - Phone (10 digits)
   - Gender
   - Date of Birth
   - Password
   - Confirm Password

3. **Click "Register"**
4. **Check the console logs** - you should see:
   ```
   API Base URL: http://10.0.2.2:5000/api
   Platform: android
   Making POST request to: http://10.0.2.2:5000/api/auth/register
   ```

5. **If successful:**
   - Registration modal closes
   - Login modal opens
   - You can now login!

✅ Registration works!

6. **To login:**
   - Enter your username and password
   - Click "Login"
   - You should be redirected to the home screen

✅ Login works!

---

## ✅ Verification Checklist

- [ ] Firewall rule created ("Flask Backend Port 5000")
- [ ] Backend running on port 5000 (see terminal output)
- [ ] Backend health check works (http://localhost:5000/api/health)
- [ ] Frontend started (Expo Dev Tools visible)
- [ ] App running on Android emulator/device
- [ ] Registration works (no "Network request failed" error)
- [ ] Login works (redirects to home screen)

---

## 🐛 Troubleshooting

### If you still see "Network request failed":

1. **Check backend is running:**
   - Look at backend terminal - should show "Running on http://0.0.0.0:5000"
   - If not, restart it

2. **Test backend in browser:**
   - Go to http://localhost:5000/api/health
   - If it doesn't load, firewall might still be blocking

3. **Check console logs:**
   - Look for "API Base URL" and "Making POST request" logs
   - If you don't see these, the app might not be making requests

4. **Try restarting everything:**
   - Stop backend (Ctrl+C)
   - Restart backend (`python app.py`)
   - Reload app (press `r` in Expo terminal)

### If registration works but login doesn't redirect:

- Check if you're using the correct username (case-sensitive)
- Check console for any error messages
- Make sure the home route exists (`app/home.js`)

---

## 🎉 Success!

Once all steps are complete, your app should be fully functional:
- ✅ Register new users
- ✅ Login existing users
- ✅ Navigate to home screen
- ✅ All API calls working

Your project is now running successfully! 🚀



















