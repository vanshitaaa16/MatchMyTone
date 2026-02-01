# 🚀 ngrok Setup - Step by Step (On Your Computer)

## Step 1: Download ngrok (On Computer)

1. **Open browser on your COMPUTER**
2. Go to: **https://ngrok.com/download**
3. Click **"Download for Windows"**
4. Save the ZIP file (e.g., to Downloads folder)

---

## Step 2: Extract ngrok (On Computer)

1. **Find the ZIP file** you just downloaded
2. **Right-click** → **"Extract All"**
3. Choose location: `C:\ngrok\` (or any folder you remember)
4. Click **"Extract"**
5. You should see `ngrok.exe` in that folder

---

## Step 3: Start ngrok (On Computer)

1. **Open Command Prompt** on your computer:
   - Press `Win + R`
   - Type `cmd` and press Enter

2. **Navigate to ngrok folder:**
   ```bash
   cd C:\ngrok
   ```
   (Or wherever you extracted ngrok)

3. **Start ngrok:**
   ```bash
   ngrok http 5000
   ```

4. **You'll see output like:**
   ```
   Session Status                online
   Forwarding   https://abc123-def456.ngrok-free.app -> http://localhost:5000
   ```

5. **Copy the HTTPS URL** (the one starting with `https://`)

---

## Step 4: Update Your App Code (On Computer)

1. **Open `src/api.js`** in your project
2. **Find line 11:**
   ```javascript
   return 'http://192.168.31.111:5000/api';
   ```

3. **Replace with your ngrok URL:**
   ```javascript
   return 'https://abc123-def456.ngrok-free.app/api';
   ```
   (Use YOUR actual ngrok URL!)

4. **Save the file**

---

## Step 5: Test (On Phone)

1. **Keep ngrok running** (don't close that terminal!)
2. **On your phone browser**, try:
   ```
   https://abc123-def456.ngrok-free.app/api/health
   ```
   (Use YOUR ngrok URL)

3. **Should see:** `{"status": "ok", "message": "API is running"}` ✅

4. **In your Expo app**, reload (press `r` in Expo terminal)
5. **Try login** - should work now! ✅

---

## 📱 Your Phone:
- ❌ **NO download needed**
- ❌ **NO app needed**
- ✅ **Just works!** Uses the URL from your code

---

## Keep ngrok Running:
- **Keep the ngrok terminal open** while developing
- If you close it, the URL stops working
- Restart ngrok to get a new URL (update code if needed)

---

## That's It! 🎉

Your app will now work from anywhere, no network issues!



