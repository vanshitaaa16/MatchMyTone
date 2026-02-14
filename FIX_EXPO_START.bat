@echo off
echo ========================================
echo   Fixing Expo Start Issues
echo ========================================
echo.

echo Step 1: Stopping any running Expo processes...
taskkill /F /IM node.exe 2>nul
timeout /t 2 /nobreak >nul
echo.

echo Step 2: Clearing npm cache...
call npm cache clean --force
echo.

echo Step 3: Reinstalling dependencies...
call npm install
echo.

echo Step 4: Starting Expo with cleared cache...
echo.
echo ========================================
echo   Starting Expo...
echo ========================================
echo.
call npx expo start --clear

pause











