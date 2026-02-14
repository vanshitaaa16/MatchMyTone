# ✅ DO THIS NOW - Step by Step

## I've Updated Your Code!

I changed `src/api.js` to use your IP address: `192.168.31.111`

## Follow These Steps EXACTLY:

### Step 1: Fix Windows Firewall (MOST IMPORTANT!)

**Right-click `FIX_FIREWALL_NOW.bat` → "Run as administrator"**

This is the #1 reason it's not working!

### Step 2: Restart Your Backend

1. **Stop backend** (press Ctrl+C in backend terminal)
2. **Start backend again:**
   ```bash
   cd backend
   python app.py
   ```
3. **Verify you see:**
   ```
   * Running on http://0.0.0.0:5000
   * Running on http://192.168.31.111:5000
   ```

### Step 3: Clear App Cache and Reload

**In your Expo terminal:**
1. Press `Shift + R` (capital R) - this clears cache and reloads
2. **OR** stop Expo (Ctrl+C) and restart:
   ```bash
   npm start -- --clear
   ```

### Step 4: Test Backend from Browser

**Open browser and go to:**
```
http://192.168.31.111:5000/api/health
```

**You should see:**
```json
{"status": "ok", "message": "API is running"}
```

**If this doesn't work:** The firewall is blocking it. Run `FIX_FIREWALL_NOW.bat` as administrator.

### Step 5: Try Login Again

1. Close the app completely on your device
2. Reopen it
3. Try to login

## What I Changed:

✅ Updated `src/api.js` to use: `http://192.168.31.111:5000/api`

## If Still Not Working:

**Run the diagnostic:**
```bash
FIX_CONNECTION_COMPLETE.bat
```

**Check:**
1. Are you using Android emulator or physical device?
2. If physical device: Is it on the same Wi-Fi network?
3. Did you run the firewall fix as administrator?

## Quick Test:

**Test if backend is accessible:**
- Open browser on your computer
- Go to: `http://192.168.31.111:5000/api/health`
- If this works → Backend is fine, it's an app/network issue
- If this doesn't work → Firewall is blocking, run `FIX_FIREWALL_NOW.bat`




