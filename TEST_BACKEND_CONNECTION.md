# Test Backend Connection

## Your Setup
- Backend: `http://192.168.31.111:5000` ✅ Running
- App trying: `http://192.168.31.111:5000/api` ✅ Correct
- Firewall: Rules exist ✅

## Possible Issues

### 1. Phone and Computer on Different Networks
**Check:** Make sure your phone and computer are on the **SAME Wi-Fi network**

### 2. Test Connection from Phone
1. Open a browser on your phone
2. Go to: `http://192.168.31.111:5000/api/health`
3. You should see: `{"status": "ok", "message": "API is running"}`
4. If this doesn't work, the phone can't reach your computer

### 3. Try Using Your Computer's IP
Your computer has multiple IPs:
- `192.168.31.111` (main Wi-Fi)
- `192.168.239.1` (virtual adapter)
- `192.168.41.1` (another virtual adapter)

Make sure your phone is on the same network as `192.168.31.111`

### 4. Alternative: Use Expo Tunnel for Backend
If network issues persist, we can set up a tunnel for the backend too.



