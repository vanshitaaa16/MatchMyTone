# 🚀 Use ngrok - Bypass All Network Issues!

## Why ngrok?
- Works even if phone and computer are on different networks
- Bypasses Windows Firewall
- Bypasses router restrictions
- Works from anywhere!

## Setup (5 Minutes)

### Step 1: Download ngrok
1. Go to: https://ngrok.com/download
2. Download for Windows
3. Extract the ZIP file
4. Copy `ngrok.exe` to a folder (e.g., `C:\ngrok\`)

### Step 2: Get Free Account (Optional but Recommended)
1. Go to: https://dashboard.ngrok.com/signup
2. Sign up (free)
3. Get your authtoken from dashboard
4. Run: `ngrok config add-authtoken YOUR_TOKEN`

### Step 3: Start ngrok Tunnel
1. Open terminal in the folder with `ngrok.exe`
2. Run:
   ```bash
   ngrok http 5000
   ```
3. You'll see:
   ```
   Forwarding   https://abc123.ngrok.io -> http://localhost:5000
   ```

### Step 4: Update Your App
1. Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`)
2. Open `src/api.js`
3. Update:
   ```javascript
   const getApiBaseUrl = () => {
     if (__DEV__) {
       if (Platform.OS === 'android') {
         return 'https://abc123.ngrok.io/api';  // Your ngrok URL
       }
       // ... rest of code
     }
   };
   ```

### Step 5: Restart App
1. Reload your Expo app (press `r` in terminal)
2. Try login again
3. It should work! ✅

---

## Keep ngrok Running
- Keep the ngrok terminal open while developing
- The URL changes each time you restart ngrok (unless you have a paid plan)
- Update `src/api.js` with the new URL if it changes

---

## Test ngrok
1. Open ngrok URL in phone browser: `https://abc123.ngrok.io/api/health`
2. Should see: `{"status": "ok", "message": "API is running"}`

If this works, update your app and it will work too!



