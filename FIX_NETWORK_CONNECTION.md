# Fix "Failed to download remote update" Error

## The Problem
Expo Go cannot connect to your Metro bundler. This is a **network connection issue**.

## Solutions (Try in Order)

### Solution 1: Check Network Connection
1. **Make sure your phone and computer are on the SAME Wi-Fi network**
2. **Check if firewall is blocking** - Windows Firewall might be blocking port 8081
3. **Try using tunnel mode** instead of LAN

### Solution 2: Use Tunnel Mode
In your Expo terminal, press `s` to switch connection modes, then select **"tunnel"**

Or restart with tunnel:
```bash
npx expo start --tunnel
```

### Solution 3: Check IP Address
1. In Expo terminal, it shows: `exp://192.168.31.111:8081`
2. Make sure this IP matches your computer's IP
3. To check your IP: Run `ipconfig` in terminal and look for IPv4 address

### Solution 4: Disable Firewall Temporarily
1. Open Windows Defender Firewall
2. Temporarily disable it
3. Try connecting again
4. Re-enable after testing

### Solution 5: Use USB Connection (Android)
If using Android:
1. Connect phone via USB
2. Enable USB debugging
3. Run: `npx expo start --android`

## Quick Fix Commands

```bash
# Stop current server (Ctrl+C)
# Then try tunnel mode:
npx expo start --tunnel --clear
```

Or try LAN with specific port:
```bash
npx expo start --lan --clear
```



