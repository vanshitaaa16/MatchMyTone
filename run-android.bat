@echo off
echo ========================================
echo   Running MatchMyTone on Android
echo ========================================
echo.
echo IMPORTANT: This project uses native modules (camera, face-detector)
echo and requires a DEVELOPMENT BUILD, not Expo Go!
echo.
echo ========================================
echo.

REM Check if Android emulator/device is available
echo Checking for Android devices/emulators...
call adb devices
echo.

echo Step 1: Prebuilding native code...
echo (This may take a few minutes the first time)
echo.
call npx expo prebuild --clean
echo.

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Prebuild failed!
    echo Make sure you have Android Studio installed and configured.
    pause
    exit /b 1
)

echo.
echo Step 2: Building and running on Android...
echo Note: Make sure you have an Android emulator running or a device connected!
echo.
call npx expo run:android

pause

