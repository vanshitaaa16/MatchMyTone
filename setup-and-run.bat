@echo off
echo ========================================
echo   MatchMyTone - Setup and Run Script
echo ========================================
echo.

REM Step 1: Install dependencies
echo [Step 1/3] Installing npm dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ERROR: npm install failed!
    pause
    exit /b 1
)
echo ✓ Dependencies installed successfully!
echo.

REM Step 2: Prebuild (if android folder doesn't exist or needs update)
echo [Step 2/3] Running Expo prebuild...
call npx expo prebuild
if %errorlevel% neq 0 (
    echo ERROR: Prebuild failed!
    pause
    exit /b 1
)
echo ✓ Prebuild completed successfully!
echo.

REM Step 3: Start Expo
echo [Step 3/3] Starting Expo...
echo.
echo ========================================
echo   Choose how to run your app:
echo ========================================
echo   - Press 'a' for Android emulator/device
echo   - Press 'i' for iOS simulator
echo   - Press 'w' for web browser
echo   - Scan QR code with Expo Go app
echo ========================================
echo.
call npx expo start

pause

