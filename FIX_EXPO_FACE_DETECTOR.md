# How to Fix ExpoFaceDetector Error

## Quick Fix Steps (Do These in Order)

### 1. Stop Your Development Server
Press `Ctrl+C` in the terminal where Expo is running.

### 2. Update app.json (Already Done ✅)
The plugin configuration has been added to `app.json`. Verify it looks like this:

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

### 3. Rebuild Your App (REQUIRED)
**Important:** `expo-face-detector` is a native module. You MUST rebuild your app. It won't work with Expo Go.

**For Android:**
```bash
# Clean and rebuild
npx expo prebuild --clean
npx expo run:android
```

**For iOS:**
```bash
npx expo prebuild --clean
npx expo run:ios
```

### 4. Wait for Build to Complete
This will take a few minutes. The app will be installed on your device/emulator.

### 5. Start Development Server
After the build completes:
```bash
npx expo start
```

### 6. Test the Camera Screen
Navigate to the camera screen and verify face detection works.

---

## Why This Error Happens

- **Native modules** like `expo-face-detector` require native code compilation
- **Expo Go** doesn't support custom native modules
- You need a **development build** (`expo run:android` or `expo run:ios`)
- The app must be **rebuilt** after adding native modules

---

## Alternative: Test UI Without Face Detection

If you want to test the UI first before rebuilding, temporarily disable face detection:

1. In `app/ColorAnalysis/camera.js`, comment out line 15:
```javascript
// import * as FaceDetector from 'expo-face-detector';
```

2. Comment out the faceDetectorSettings prop (around line 428-434):
```javascript
// faceDetectorSettings={{
//   mode: FaceDetector.FaceDetectorMode.fast,
//   detectLandmarks: FaceDetector.FaceLandmarks.all,
//   runClassifications: FaceDetector.FaceDetectorClassifications.all,
//   minDetectionInterval: 100,
//   tracking: true,
// }}
// onFacesDetected={handleFacesDetected}
```

3. Temporarily enable validations for testing (around line 180-183):
```javascript
// For testing - remove after adding face detection back
setLightingValid(true);
setExpressionValid(true);
setAlignmentValid(true);
```

This lets you test the UI and countdown without face detection. Then rebuild with face detection later.

---

## Troubleshooting

**If rebuild fails:**
- Make sure you have Android Studio/Xcode installed
- Check that your device/emulator is connected
- Try: `npx expo prebuild --clean` again

**If still getting the error:**
- Verify `expo-face-detector` is in `package.json` dependencies
- Run: `npm install` or `npx expo install expo-face-detector`
- Make sure you're using a development build, not Expo Go

**Export error should be fixed** - The default export is already correct in the code.





