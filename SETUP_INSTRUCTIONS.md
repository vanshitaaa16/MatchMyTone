# Fixing ExpoFaceDetector Error - Setup Instructions

## The Problem
You're getting two errors:
1. **"Cannot find native module 'ExpoFaceDetector'"** - The native module isn't linked
2. **"Route missing default export"** - This should be fixed now

## Solution Steps

### Step 1: Stop the Development Server
Press `Ctrl+C` in your terminal to stop the Expo dev server.

### Step 2: Clear Cache and Reinstall Dependencies
Run these commands in your project root:

```bash
# Clear Expo cache
npx expo start --clear

# Or if that doesn't work, try:
npm install
npx expo install expo-face-detector
```

### Step 3: Rebuild the Native App
Since `expo-face-detector` is a native module, you need to rebuild your app:

**For Android:**
```bash
# Stop the dev server first (Ctrl+C)
npx expo prebuild --clean
npx expo run:android
```

**For iOS (if testing on iOS):**
```bash
npx expo prebuild --clean
npx expo run:ios
```

**OR use EAS Build (if you're using EAS):**
```bash
eas build --platform android
```

### Step 4: Verify app.json Configuration
Make sure your `app.json` has the expo-face-detector plugin configured (already done):
```json
"plugins": [
  "expo-router",
  "expo-font",
  [
    "expo-face-detector",
    {
      "cameraPermission": "Allow $(PRODUCT_NAME) to access your camera to take selfies for color analysis."
    }
  ]
]
```

### Step 5: Restart Development Server
After rebuilding:
```bash
npx expo start
```

## Alternative: Test Without Face Detection First

If you want to test the camera UI first without face detection (to verify the export issue is fixed), you can temporarily comment out the face detection code:

1. Comment out the import:
```javascript
// import * as FaceDetector from 'expo-face-detector';
```

2. Comment out faceDetectorSettings and onFacesDetected props in CameraView

3. Set all validations to true temporarily for testing:
```javascript
setLightingValid(true);
setExpressionValid(true);
setAlignmentValid(true);
```

Then rebuild later when ready.

## Important Notes

- **Native modules require a rebuild** - You cannot use `expo-face-detector` with Expo Go. You must build a development build or production build.
- **Development Build Required** - Use `npx expo run:android` or `npx expo run:ios` to create a development build that includes native modules.
- **Expo Go Limitation** - Expo Go doesn't support custom native modules like `expo-face-detector`. You need a development build.

## Quick Fix Summary

1. Stop server (Ctrl+C)
2. Run: `npx expo prebuild --clean`
3. Run: `npx expo run:android` (or `run:ios`)
4. Wait for build to complete
5. Start server: `npx expo start`
6. Test the camera screen

The export issue should already be fixed in the code. The main issue is the native module needs to be rebuilt.
