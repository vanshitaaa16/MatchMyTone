# 🔴 IMMEDIATE FIX for "Failed to download remote update"

## The Problem
Expo Go cannot connect to your Metro bundler. This is a **network/firewall issue**.

## ✅ QUICK FIX (Try This First!)

### Option 1: Use Tunnel Mode (Easiest - Works Everywhere!)

1. **Stop your current Expo server** (Press `Ctrl+C`)

2. **Start with tunnel mode:**
   ```bash
   npx expo start --tunnel --clear
   ```

3. **Wait for it to connect** (may take 30-60 seconds)

4. **Scan the NEW QR code** with Expo Go

**Tunnel mode works even if firewall blocks your connection!**

---

### Option 2: Fix Firewall (If Tunnel Doesn't Work)

1. **Open Windows Defender Firewall:**
   - Press `Win + R`
   - Type `wf.msc` and press Enter

2. **Allow Node.js through Firewall:**
   - Click "Allow an app or feature through Windows Defender Firewall"
   - Click "Change settings"
   - Find "Node.js" in the list
   - Check both "Private" and "Public" boxes
   - Click OK

3. **Or create a rule for port 8081:**
   - Click "Advanced settings"
   - Click "Inbound Rules" → "New Rule"
   - Select "Port" → Next
   - Select "TCP" and enter "8081" in "Specific local ports"
   - Select "Allow the connection"
   - Check all profiles (Domain, Private, Public)
   - Name it "Expo Metro Bundler"
   - Click Finish

4. **Restart Expo:**
   ```bash
   npx expo start --clear
   ```

---

### Option 3: Check Network Connection

1. **Make sure phone and computer are on the SAME Wi-Fi network**
   - Your computer IP: `192.168.31.111`
   - Your phone must be on the same network

2. **Try disconnecting and reconnecting Wi-Fi on your phone**

3. **Restart Expo:**
   ```bash
   npx expo start --clear
   ```

---

## 🚀 Recommended: Use Tunnel Mode

**Tunnel mode is the easiest solution** - it works even with firewalls!

Just run:
```bash
npx expo start --tunnel --clear
```

Then scan the new QR code!

---

## Still Not Working?

1. **Check if port 8081 is in use:**
   ```bash
   netstat -ano | findstr :8081
   ```

2. **Try a different port:**
   ```bash
   npx expo start --port 8082 --clear
   ```

3. **Share the exact error message** you see in Expo Go



