# 🚨 URGENT FIX - Connection Still Not Working

## Your IP Address: `192.168.31.111`

I found your computer's IP address. Let's fix this step by step.

## Step 1: Update API URL in Code

**Open `src/api.js` and change line 13:**

**For Android Emulator (if 10.0.2.2 doesn't work):**
```javascript
return 'http://192.168.31.111:5000/api';
```

**For Physical Android Device:**
```javascript
return 'http://192.168.31.111:5000/api';
```

**Current code shows:** `return 'http://10.0.2.2:5000/api';`

**Change it to:** `return 'http://192.168.31.111:5000/api';`

## Step 2: Fix Windows Firewall (CRITICAL)

**Run this as Administrator:**
1. Right-click `FIX_FIREWALL_NOW.bat`
2. Select "Run as administrator"
3. This will allow port 5000 through firewall

**OR manually:**
1. Press `Win + R`, type `wf.msc`, press Enter
2. Click "Inbound Rules" → "New Rule"
3. Select "Port" → Next
4. Select "TCP" → Enter "5000" → Next
5. Select "Allow the connection" → Next
6. Check all (Domain, Private, Public) → Next
7. Name: "Flask Backend 5000" → Finish

## Step 3: Restart Backend

**Stop backend (Ctrl+C), then start again:**
```bash
cd backend
python app.py
```

**Make sure you see:**
```
* Running on http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
* Running on http://192.168.31.111:5000
```

## Step 4: Clear App Cache and Reload

**In Expo terminal:**
1. Press `Shift + R` (capital R) to clear cache and reload
2. OR stop Expo (Ctrl+C) and restart: `npm start -- --clear`

**In the app:**
1. Close the app completely
2. Reopen it
3. Try login again

## Step 5: Verify Connection

**Test from your computer browser:**
```
http://192.168.31.111:5000/api/health
```

**Should see:**
```json
{"status": "ok", "message": "API is running"}
```

**If this doesn't work:** Backend isn't accessible on your network IP.

## Step 6: Check Network

**If using Physical Device:**
- Make sure your phone and computer are on the **SAME Wi-Fi network**
- Check Wi-Fi settings on your phone
- Try disconnecting and reconnecting to Wi-Fi

**If using Emulator:**
- Try both `10.0.2.2` and `192.168.31.111`
- Some emulators need the actual IP instead of 10.0.2.2

## Alternative: Test with ngrok (Works Everywhere!)

If nothing else works, use ngrok to create a tunnel:

1. **Download ngrok:** https://ngrok.com/download
2. **Run ngrok:**
   ```bash
   ngrok http 5000
   ```
3. **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)
4. **Update `src/api.js`:**
   ```javascript
   return 'https://YOUR_NGROK_URL.ngrok.io/api';
   ```
5. **Reload app**

This bypasses all network/firewall issues!

## Still Not Working?

**Run the diagnostic script:**
```bash
FIX_CONNECTION_COMPLETE.bat
```

**Share with me:**
1. What IP address you're using in `src/api.js`
2. Output of `netstat -ano | findstr :5000`
3. What you see when opening `http://192.168.31.111:5000/api/health` in browser
4. Are you using emulator or physical device?




