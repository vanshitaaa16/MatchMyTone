# 🚀 Setup ngrok - Works Everywhere!

## Why ngrok?
- Bypasses Windows Firewall
- Works even if phone and computer are on different networks
- No router configuration needed
- Works from anywhere!

## Quick Setup (3 Steps)

### Step 1: Download ngrok
1. Go to: https://ngrok.com/download
2. Download **Windows 64-bit** (or 32-bit if needed)
3. Extract the ZIP file
4. Copy `ngrok.exe` to: `C:\ngrok\` (or any folder you remember)

### Step 2: Start ngrok Tunnel
1. Open Command Prompt or PowerShell
2. Navigate to where ngrok.exe is:
   ```bash
   cd C:\ngrok
   ```
3. Run:
   ```bash
   ngrok http 5000
   ```
4. You'll see something like:
   ```
   Forwarding   https://abc123-def456.ngrok-free.app -> http://localhost:5000
   ```

### Step 3: Update Your App
1. **Copy the HTTPS URL** (e.g., `https://abc123-def456.ngrok-free.app`)
2. Open `src/api.js`
3. Find this line (around line 11):
   ```javascript
   return 'http://192.168.31.111:5000/api';
   ```
4. Replace it with:
   ```javascript
   return 'https://abc123-def456.ngrok-free.app/api';  // Your ngrok URL
   ```
5. **Save the file**
6. **Reload your Expo app** (press `r` in Expo terminal)

### Step 4: Test
1. **On your phone browser**, try:
   ```
   https://abc123-def456.ngrok-free.app/api/health
   ```
2. Should see: `{"status": "ok", "message": "API is running"}` ✅
3. **Try login in your app** - should work now! ✅

---

## Keep ngrok Running
- **Keep the ngrok terminal open** while developing
- The URL is free and works as long as ngrok is running
- If you restart ngrok, you'll get a new URL (update `src/api.js`)

---

## That's It!
Your app will now work from anywhere, bypassing all network issues!



