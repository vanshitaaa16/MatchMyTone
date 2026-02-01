# Network Connection Troubleshooting

## Issue: "Network request failed" on Android Emulator

If you're seeing "Network request failed" errors when trying to register/login, follow these steps:

### Step 1: Verify Backend is Running

Make sure your Flask backend is running:
```bash
cd backend
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
```

### Step 2: Test Backend Health Endpoint

Open a browser or use curl to test:
```
http://localhost:5000/api/health
```

You should see: `{"status": "ok", "message": "API is running"}`

### Step 3: Check Windows Firewall

**The most common issue is Windows Firewall blocking port 5000.**

1. **Open Windows Defender Firewall:**
   - Press `Win + R`
   - Type `wf.msc` and press Enter

2. **Allow Python through Firewall:**
   - Click "Allow an app or feature through Windows Defender Firewall"
   - Find "Python" in the list
   - Check both "Private" and "Public" boxes
   - Click OK

3. **Or create a rule for port 5000:**
   - Click "Advanced settings"
   - Click "Inbound Rules" → "New Rule"
   - Select "Port" → Next
   - Select "TCP" and enter "5000" in "Specific local ports"
   - Select "Allow the connection"
   - Check all profiles (Domain, Private, Public)
   - Name it "Flask Backend Port 5000"
   - Click Finish

### Step 4: Verify API URL

The app automatically uses:
- **Android Emulator**: `http://10.0.2.2:5000/api`
- **iOS Simulator**: `http://localhost:5000/api`

Check the console logs - you should see:
```
API Base URL: http://10.0.2.2:5000/api
Platform: android
```

### Step 5: Test from Android Emulator

If you have `adb` installed, you can test connectivity:
```bash
adb shell
curl http://10.0.2.2:5000/api/health
```

### Step 6: Alternative - Use Your Computer's IP Address

If `10.0.2.2` doesn't work, try using your computer's local IP:

1. **Find your IP address:**
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" under your network adapter (usually `192.168.x.x`)

2. **Update `src/api.js`:**
   ```javascript
   if (Platform.OS === 'android') {
     return 'http://192.168.x.x:5000/api';  // Replace x.x with your IP
   }
   ```

3. **Make sure Flask is binding to all interfaces:**
   In `backend/app.py`, ensure:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```

### Step 7: Restart Everything

After making changes:
1. Stop the backend (Ctrl+C)
2. Restart the backend
3. Reload your React Native app (press `r` in the Expo terminal)

### Still Not Working?

1. Check if another app is using port 5000:
   ```bash
   netstat -ano | findstr :5000
   ```

2. Try a different port (e.g., 5001):
   - Update `backend/app.py`: `app.run(debug=True, host='0.0.0.0', port=5001)`
   - Update `src/api.js`: Change port from 5000 to 5001

3. Check backend logs for errors when making a request

4. Try using a physical device instead of emulator (use your computer's IP address)



















