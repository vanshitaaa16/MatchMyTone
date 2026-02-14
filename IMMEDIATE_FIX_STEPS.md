# 🚨 IMMEDIATE FIX - Connection Error

## Your Backend is Running ✅
I can see your backend is listening on port 5000 correctly.

## The Problem
The Android emulator can't reach your backend even though it's running.

## Quick Fix (Try This First)

### Step 1: Test Backend from Browser
Open your browser and go to:
```
http://localhost:5000/api/health
```

**If this works:** Backend is fine, it's an emulator connection issue.
**If this doesn't work:** Backend isn't actually responding, restart it.

### Step 2: Check Windows Firewall
The most common issue is Windows Firewall blocking the connection.

**Quick Fix:**
1. When you start the backend, Windows should show a popup asking to allow Python through firewall
2. **Click "Allow access"** for both Private and Public networks
3. If you didn't see the popup, do this manually:

**Manual Firewall Fix:**
1. Press `Win + R`, type `wf.msc`, press Enter
2. Click "Inbound Rules" → "New Rule"
3. Select "Port" → Next
4. Select "TCP" → Enter "5000" → Next
5. Select "Allow the connection" → Next
6. Check all (Domain, Private, Public) → Next
7. Name: "Flask Backend 5000" → Finish

### Step 3: Restart Backend
After firewall changes, restart your backend:
```bash
# Stop backend (Ctrl+C)
# Then start again:
cd backend
python app.py
```

### Step 4: Try Using Your Computer's IP
If `10.0.2.2` still doesn't work, try using your actual IP address:

1. **Find your IP:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., `192.168.1.100`)

2. **Update `src/api.js` line 12:**
   ```javascript
   if (Platform.OS === 'android') {
     return 'http://YOUR_IP_HERE:5000/api';  // Replace with your IP
   }
   ```

3. **Reload the app:**
   - Press `r` in Expo terminal
   - Or restart the app

### Step 5: Test Connection
Run the test script:
```bash
TEST_BACKEND_CONNECTION.bat
```

## What I Fixed

1. ✅ **Added default exports** to `geminiConfig.js` and `colorAnalysisGemini.js` to fix route warnings
2. ✅ **Verified backend is listening** on `0.0.0.0:5000` (correct)
3. ✅ **Created test script** to diagnose connection issues

## Most Likely Solution

**Windows Firewall is blocking the connection.** 

Do this:
1. Allow Python through firewall (see Step 2 above)
2. Restart backend
3. Try login again

The backend is running correctly - it's just being blocked by Windows Firewall!




