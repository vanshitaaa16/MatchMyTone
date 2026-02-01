# 🔧 Fix "Network request failed" Error

## Quick Fix Steps

### 1. **Allow Python/Flask through Windows Firewall** ⚠️ MOST IMPORTANT

This is the most common cause! Windows Firewall is blocking port 5000.

**Method 1: Quick Fix (Recommended)**
1. When you start the backend (`python app.py`), Windows will show a popup asking "Windows Defender Firewall has blocked some features of this app"
2. **Click "Allow access"** on both Private and Public networks
3. Restart the backend if needed

**Method 2: Manual Firewall Rule**
1. Press `Win + R`, type `wf.msc`, press Enter
2. Click "Inbound Rules" → "New Rule"
3. Select "Port" → Next
4. Select "TCP" → Enter "5000" in "Specific local ports" → Next
5. Select "Allow the connection" → Next
6. Check all (Domain, Private, Public) → Next
7. Name: "Flask Backend 5000" → Finish

### 2. **Restart Your Backend**

Stop the backend (Ctrl+C) and restart:
```bash
cd backend
python app.py
```

Make sure you see:
```
* Running on http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
```

### 3. **Test the Backend**

Open your browser and go to:
```
http://localhost:5000/api/health
```

You should see:
```json
{"status": "ok", "message": "API is running"}
```

If this doesn't work, the firewall is blocking it.

### 4. **Check Console Logs**

When you try to register/login, check the console logs. You should see:
```
API Base URL: http://10.0.2.2:5000/api
Platform: android
Making POST request to: http://10.0.2.2:5000/api/auth/register
```

If you don't see the "Making POST request" log, the request isn't being sent.

### 5. **Reload Your App**

After fixing the firewall, reload your React Native app:
- Press `r` in the Expo terminal to reload

---

## ✅ Verification Checklist

- [ ] Windows Firewall allows Python/port 5000
- [ ] Backend is running (see "Running on http://0.0.0.0:5000")
- [ ] `http://localhost:5000/api/health` works in browser
- [ ] Console shows correct API URL (`http://10.0.2.2:5000/api`)
- [ ] App reloaded after changes

If all checked, try registering/login again! 🎉



















