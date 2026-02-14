# 🔴 URGENT: Fix "Cannot Connect to Server" Error

## The Problem
Your backend is running, but the app still shows "Cannot connect to server" error.

## Quick Fixes (Try in Order)

### Fix 1: Verify Backend is Actually Listening

**Check if backend is listening on port 5000:**
```bash
netstat -ano | findstr :5000
```

You should see something like:
```
TCP    0.0.0.0:5000    0.0.0.0:0    LISTENING    12345
```

**If you see `127.0.0.1:5000` instead of `0.0.0.0:5000`, that's the problem!**

The backend must listen on `0.0.0.0` (all interfaces), not just `127.0.0.1` (localhost only).

**Fix:** Make sure `backend/app.py` has:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Fix 2: Test Backend from Browser

**On your computer, open browser and go to:**
```
http://localhost:5000/api/health
```

**You should see:**
```json
{"status": "ok", "message": "API is running"}
```

**If this doesn't work:**
- Backend isn't actually running
- Or it's not listening on the right interface
- Restart the backend

### Fix 3: Test from Android Emulator

**The app is trying to connect to:** `http://10.0.2.2:5000/api`

**Test this manually:**
1. Open a terminal in your Android emulator (if possible)
2. Or use ADB:
```bash
adb shell
curl http://10.0.2.2:5000/api/health
```

**If this fails:**
- The emulator can't reach your host machine
- Try using your computer's actual IP address instead

### Fix 4: Use Your Computer's IP Address

**Find your IP:**
```bash
ipconfig
```

Look for "IPv4 Address" (e.g., `192.168.1.100`)

**Update `src/api.js` line 12:**
```javascript
if (Platform.OS === 'android') {
  return 'http://YOUR_IP_ADDRESS:5000/api';  // Replace with your IP
}
```

**Then restart the app:**
- Press `r` in Expo terminal to reload
- Or restart the app completely

### Fix 5: Windows Firewall

**Even if backend is running, Windows Firewall might be blocking:**

1. **Check if Python is allowed:**
   - Press `Win + R`
   - Type `wf.msc` and press Enter
   - Click "Inbound Rules"
   - Look for "Python" or "python.exe"
   - Make sure it's **ENABLED** and allows **Port 5000**

2. **Create a new rule if needed:**
   - Click "New Rule"
   - Select "Port" → Next
   - Select "TCP" → Enter "5000" → Next
   - Select "Allow the connection" → Next
   - Check all (Domain, Private, Public) → Next
   - Name: "Flask Backend 5000" → Finish

3. **Restart backend after firewall changes**

### Fix 6: Restart Everything

**Sometimes a clean restart fixes it:**

1. **Stop backend** (Ctrl+C)
2. **Stop Expo** (Ctrl+C)
3. **Kill any stuck processes:**
   ```bash
   taskkill /F /IM python.exe
   taskkill /F /IM node.exe
   ```
4. **Start backend:**
   ```bash
   cd backend
   python app.py
   ```
5. **Start Expo:**
   ```bash
   npm start
   ```
6. **Reload app** (press `r` in Expo terminal)

## Verification Checklist

After trying fixes, verify:

- [ ] Backend shows: `* Running on http://0.0.0.0:5000`
- [ ] `netstat` shows: `TCP    0.0.0.0:5000    LISTENING`
- [ ] Browser test works: `http://localhost:5000/api/health`
- [ ] Windows Firewall allows Python/port 5000
- [ ] App console shows: `API Base URL: http://10.0.2.2:5000/api`
- [ ] Backend terminal shows incoming requests when you try to login

## Still Not Working?

**Share these details:**
1. Output of `netstat -ano | findstr :5000`
2. What you see when opening `http://localhost:5000/api/health` in browser
3. Backend terminal output when you try to login
4. Expo terminal output (any errors?)




