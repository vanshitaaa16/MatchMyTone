# 📱 Complete Guide: Setting Up Development Build for FaceID Camera

## Overview
Your FaceID-style camera requires native modules (`expo-camera` + `expo-face-detector`), so you need a **development build**. This guide will walk you through everything step-by-step.

---

## Part 1: Install Android Studio

### Step 1: Download Android Studio
1. Go to: https://developer.android.com/studio
2. Click **"Download Android Studio"**
3. Download the installer for Windows
4. File size: ~1 GB (download may take 10-20 minutes)

### Step 2: Install Android Studio
1. **Run the installer** (android-studio-*.exe)
2. Click **"Next"** through the setup wizard
3. **Important:** Make sure these are checked:
   - ✅ Android SDK
   - ✅ Android SDK Platform
   - ✅ Android Virtual Device
4. Click **"Next"** → **"Install"**
5. Wait for installation (10-15 minutes)
6. Click **"Finish"** when done

### Step 3: First Launch Setup
1. **Launch Android Studio**
2. If asked to import settings, choose **"Do not import settings"**
3. Click **"Next"** through the setup wizard
4. Choose **"Standard"** installation type
5. Accept license agreements
6. Click **"Finish"**
7. Wait for components to download (5-10 minutes)
8. Click **"Finish"** when complete

---

## Part 2: Set Up Android Emulator

### Step 1: Open AVD Manager
1. In Android Studio, click **"More Actions"** → **"Virtual Device Manager"**
   OR
   Click the **phone icon** in the top toolbar

### Step 2: Create Virtual Device
1. Click **"+ Create Device"** button
2. **Choose a device:**
   - Select **"Phone"** category
   - Choose **"Pixel 5"** or **"Pixel 6"** (recommended)
   - Click **"Next"**

### Step 3: Download System Image
1. **Select a system image:**
   - Choose **"Tiramisu"** (API 33) or **"UpsideDownCake"** (API 34)
   - Click the **download icon** next to it
   - Wait for download (2-5 GB, may take 20-40 minutes)
   - Click **"Next"** when download completes

### Step 4: Configure Virtual Device
1. **Verify configuration:**
   - Name: "Pixel_5_API_33" (or similar)
   - Click **"Finish"**

### Step 5: Start Emulator
1. In Virtual Device Manager, click the **▶️ Play button** next to your device
2. Wait for emulator to start (2-5 minutes first time)
3. You should see an Android phone screen appear

**✅ Emulator is now running!** Keep it open.

---

## Part 3: Build Your App

### Step 1: Open Terminal in Your Project
1. Open **PowerShell** or **Command Prompt**
2. Navigate to your project:
   ```bash
   cd "C:\Users\VANSHITA SHAH\MatchMyTone"
   ```

### Step 2: Install Dependencies (if needed)
```bash
npm install
```

### Step 3: Generate Native Code
```bash
npx expo prebuild --clean
```

**When asked about Git changes:**
- Type **"yes"** and press Enter
- This is safe - it's just generating native code files

**Wait for completion** (2-5 minutes)

### Step 4: Build and Run on Emulator
```bash
npx expo run:android
```

**What happens:**
1. Gradle will download dependencies (first time: 10-20 minutes)
2. App will compile (5-10 minutes)
3. App will automatically install on your emulator
4. App will launch automatically

**✅ Your app is now running with native modules!**

---

## Part 4: Alternative - Use Physical Phone

If you prefer using your physical Android phone instead of emulator:

### Step 1: Enable Developer Options
1. On your phone, go to **Settings** → **About Phone**
2. Find **"Build Number"**
3. **Tap it 7 times** until you see "You are now a developer!"

### Step 2: Enable USB Debugging
1. Go back to **Settings**
2. Find **"Developer Options"** (usually under System)
3. Turn on **"USB Debugging"**
4. Turn on **"Install via USB"** (if available)

### Step 3: Connect Phone
1. Connect phone to computer via USB cable
2. On phone, when prompted, tap **"Allow USB Debugging"** → **"Always allow"**
3. Check **"Always allow from this computer"**

### Step 4: Verify Connection
```bash
adb devices
```

You should see your device listed. If not:
- Try different USB cable
- Try different USB port
- Make sure USB debugging is enabled

### Step 5: Build and Run
```bash
npx expo prebuild --clean
```
(Answer "yes" to Git question)

```bash
npx expo run:android
```

App will install on your phone automatically!

---

## Part 5: Start Development Server

After the app is installed and running:

### Step 1: Start Metro Bundler
In a **new terminal window**:
```bash
cd "C:\Users\VANSHITA SHAH\MatchMyTone"
npx expo start
```

### Step 2: Test Your App
1. In the app on emulator/phone, navigate to **Color Analysis**
2. Click **"Take a selfie"**
3. You should see the FaceID-style camera interface!
4. Position your face in the oval
5. Watch validation indicators turn green
6. Countdown will start automatically
7. Photo will capture automatically

---

## Troubleshooting

### Problem: "No Android connected device found"
**Solution:**
- Make sure emulator is running (check Virtual Device Manager)
- OR phone is connected with USB debugging enabled
- Run `adb devices` to verify connection

### Problem: "Gradle build failed"
**Solution:**
- Make sure Android Studio is installed correctly
- Try: `npx expo prebuild --clean` again
- Check if you have enough disk space (need ~10 GB free)

### Problem: "SDK not found"
**Solution:**
- Open Android Studio
- Go to **Tools** → **SDK Manager**
- Install **Android SDK Platform 33** or **34**
- Install **Android SDK Build-Tools**

### Problem: "Out of memory" during build
**Solution:**
- Close other applications
- Increase Gradle memory:
  - Create/edit `android/gradle.properties`
  - Add: `org.gradle.jvmargs=-Xmx4096m`

### Problem: App crashes on camera screen
**Solution:**
- Make sure camera permissions are granted
- Check that `expo-camera` and `expo-face-detector` are in `package.json`
- Try rebuilding: `npx expo run:android` again

---

## Quick Reference Commands

```bash
# Navigate to project
cd "C:\Users\VANSHITA SHAH\MatchMyTone"

# Install dependencies
npm install

# Generate native code
npx expo prebuild --clean

# Build and run on Android
npx expo run:android

# Start development server (in separate terminal)
npx expo start

# Check connected devices
adb devices

# Clean build (if having issues)
npx expo prebuild --clean
cd android
./gradlew clean
cd ..
npx expo run:android
```

---

## Expected Timeline

- **Android Studio installation:** 20-30 minutes
- **Emulator setup:** 30-60 minutes (mostly downloading)
- **First build:** 20-30 minutes
- **Subsequent builds:** 5-10 minutes

**Total first-time setup: 1-2 hours**

---

## ✅ Success Checklist

- [ ] Android Studio installed
- [ ] Android emulator created and running
- [ ] `npx expo prebuild --clean` completed successfully
- [ ] `npx expo run:android` completed successfully
- [ ] App installed on emulator/phone
- [ ] Camera screen opens
- [ ] Face detection works
- [ ] Validation indicators turn green
- [ ] Countdown starts automatically
- [ ] Photo captures automatically

---

## Need Help?

If you get stuck at any step, let me know:
1. What step you're on
2. What error message you see
3. Screenshot if possible

I'll help you troubleshoot! 🚀

