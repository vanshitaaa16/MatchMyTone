# Testing Android Emulator Connection

Your backend is running and accessible! Now let's make sure the Android emulator can connect.

## Your Backend is Running On:
- `http://127.0.0.1:5000` ✅
- `http://192.168.110.205:5000` ✅

## Android Emulator Connection Options

The Android emulator should use `http://10.0.2.2:5000/api` (this is the special IP that points to your host machine's localhost).

However, if `10.0.2.2` doesn't work, you can try using your actual IP address: `192.168.110.205`

## Option 1: Use 10.0.2.2 (Standard - Try This First)

This should already be configured in `src/api.js`. The app should automatically use:
- Android: `http://10.0.2.2:5000/api`

## Option 2: Use Your Actual IP (If 10.0.2.2 Doesn't Work)

If you still get "Network request failed", update `src/api.js` to use your actual IP:

1. Open `src/api.js`
2. Find the `getApiBaseUrl` function
3. Change the Android URL to use your IP:

```javascript
if (Platform.OS === 'android') {
  return 'http://192.168.110.205:5000/api';  // Your actual IP
}
```

4. Save the file
5. Reload your app (press `r` in Expo terminal)

## Next Steps

1. Make sure your frontend is running
2. Try to register/login
3. Check the console logs - you should see the API URL being used
4. Check the backend terminal - you should see incoming requests

If you see requests in the backend terminal but still get errors, it's a different issue (like CORS or response format).



















