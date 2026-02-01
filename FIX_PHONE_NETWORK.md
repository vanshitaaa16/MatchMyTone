# 🔴 FIX: Computer Works, Phone Doesn't

## ✅ What's Working
- Backend is running ✅
- Port 5000 is listening ✅
- Computer can access `http://localhost:5000/api/health` ✅

## ❌ What's Not Working
- Phone cannot access `http://192.168.31.111:5000/api/health` ❌

## This is a Network Issue!

### Solution 1: Check Wi-Fi Networks (MOST COMMON)

**On your computer:**
1. Click Wi-Fi icon in system tray
2. Note the network name (e.g., "MyWiFi")

**On your phone:**
1. Go to Wi-Fi settings
2. Check which network you're connected to
3. **Must be the EXACT SAME network name!**

If different → Connect phone to same network as computer

---

### Solution 2: Windows Firewall - Allow Inbound Connections

Even though rules exist, they might not be working:

1. **Open Windows Firewall:**
   - Press `Win + R`
   - Type `wf.msc` and press Enter

2. **Go to "Inbound Rules"**

3. **Find "Flask Backend Port 5000" or "python.exe"**

4. **Right-click → Properties**

5. **Go to "Scope" tab:**
   - Under "Remote IP address", select **"Any IP address"**
   - Click OK

6. **Make sure rule is ENABLED** (green checkmark)

7. **Test again from phone**

---

### Solution 3: Disable Windows Firewall Temporarily (Test)

**To test if firewall is the issue:**

1. Open Windows Firewall
2. Click "Turn Windows Defender Firewall on or off"
3. Turn OFF for both "Private" and "Public" networks
4. Click OK
5. **Test from phone** - if it works, firewall was the issue!
6. **Turn firewall back ON** and fix the rules properly

---

### Solution 4: Check Router AP Isolation

Some routers have "AP Isolation" or "Client Isolation" enabled, which prevents devices from talking to each other.

**Check your router settings:**
1. Open router admin (usually `192.168.1.1` or `192.168.0.1`)
2. Look for "AP Isolation", "Client Isolation", or "Wireless Isolation"
3. **Disable it** if enabled
4. Save and restart router

---

### Solution 5: Use ngrok (Tunnel - Bypasses All Network Issues)

If network issues persist, use ngrok:

1. **Download ngrok:** https://ngrok.com/download
2. **Extract and run:**
   ```bash
   ngrok http 5000
   ```
3. **Copy the HTTPS URL** (e.g., `https://abc123.ngrok.io`)
4. **Update `src/api.js`:**
   ```javascript
   if (Platform.OS === 'android') {
     return 'https://abc123.ngrok.io/api';  // Your ngrok URL
   }
   ```
5. **Restart your Expo app**

This works from anywhere, bypasses firewalls and network issues!

---

## 🎯 Quick Test

**Try this on your phone browser:**
```
http://192.168.31.111:5000/api/health
```

**If it still doesn't work:**
1. Check if phone and computer are on same Wi-Fi
2. Try disabling Windows Firewall temporarily (to test)
3. Use ngrok as a workaround

---

## Most Likely Fix

**Check Wi-Fi networks first** - phone and computer must be on the SAME network!

Then try disabling firewall temporarily to test if that's the issue.



