# 🔴 Fix "Something went wrong" Error

## Step 1: See the Actual Error

1. **In Expo Go**, tap **"View error log"** at the bottom
2. **Copy the error message** you see
3. **Share it with me** so I can fix it

---

## Step 2: Clear Everything and Restart

### Stop Everything:
1. **Stop Expo** - Press `Ctrl+C` in the Expo terminal
2. **Stop ngrok** - Press `Ctrl+C` in the ngrok terminal (keep it running after)
3. **Stop backend** - Keep it running (don't stop it)

### Clear Cache:
```bash
npx expo start --clear
```

---

## Step 3: Common Fixes

### Fix 1: Reinstall Dependencies
```bash
npm install
```

### Fix 2: Clear Metro Cache
```bash
npx expo start --clear
```

### Fix 3: Check for Syntax Errors
Make sure all files are saved properly.

---

## Step 4: Restart Everything in Order

1. **Start backend** (if not running):
   ```bash
   cd backend
   python app.py
   ```

2. **Start ngrok** (in new terminal):
   ```bash
   ngrok http 5000
   ```

3. **Start Expo** (in new terminal):
   ```bash
   npx expo start --clear
   ```

4. **Scan QR code** in Expo Go

---

## 🎯 Quick Fix Script

I'll create a script to do all this automatically!



