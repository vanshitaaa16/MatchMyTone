# 🔴 FIX: "ERR_CONNECTION_REFUSED"

## The Problem
Your phone cannot reach `http://192.168.31.111:5000` - connection is being refused.

## ✅ Solutions (Try in Order)

### Solution 1: Verify Backend is Listening on All Interfaces

Your backend should be running with `host='0.0.0.0'` (which it is), but let's verify it's actually listening.

**Check if backend is running:**
```bash
netstat -ano | findstr :5000
```

You should see something like:
```
TCP    0.0.0.0:5000    0.0.0.0:0    LISTENING
```

If you see `127.0.0.1:5000` instead, that's the problem!

---

### Solution 2: Restart Backend Properly

1. **Stop the backend** (Ctrl+C in the backend terminal)
2. **Make sure it's running with host='0.0.0.0':**
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```
3. **Restart:**
   ```bash
   cd backend
   python app.py
   ```

---

### Solution 3: Check Windows Firewall (Again)

Even though rules exist, they might not be active:

1. Open `wf.msc`
2. Go to **"Inbound Rules"**
3. Find **"Flask Backend Port 5000"** or **"python.exe"**
4. Make sure they're **ENABLED** (green checkmark)
5. If disabled, right-click → **Enable**

---

### Solution 4: Check Network Connection

**On your computer:**
```bash
ipconfig
```

**On your phone:**
- Go to Wi-Fi settings
- Check which network you're on
- **Make sure it matches your computer's network**

Your computer IP: `192.168.31.111`
Your phone must be on the same `192.168.31.x` network!

---

### Solution 5: Test from Computer First

**On your computer browser, try:**
```
http://192.168.31.111:5000/api/health
```

If this works on computer but not phone → Network issue
If this doesn't work on computer → Backend issue

---

### Solution 6: Use ngrok (Tunnel - Works Everywhere!)

If network issues persist, use ngrok to create a public tunnel:

1. **Download ngrok:** https://ngrok.com/download
2. **Run:**
   ```bash
   ngrok http 5000
   ```
3. **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)
4. **Update `src/api.js`:**
   ```javascript
   return 'https://abc123.ngrok.io/api';
   ```

This bypasses all network/firewall issues!

---

## 🎯 Most Likely Fix

**Restart the backend** and make sure it shows:
```
* Running on http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
* Running on http://192.168.31.111:5000
```

If it only shows `127.0.0.1`, that's the problem!



