@echo off
echo ========================================
echo   Fixing Module Loading Issues
echo ========================================
echo.

echo Step 1: Clearing npm cache...
call npm cache clean --force
echo.

echo Step 2: Removing node_modules and package-lock.json...
if exist node_modules rmdir /s /q node_modules
if exist package-lock.json del /f package-lock.json
echo.

echo Step 3: Reinstalling all dependencies...
call npm install
echo.

echo Step 4: Clearing Expo cache...
call npx expo start --clear --no-dev --minify
timeout /t 3 /nobreak >nul
taskkill /F /IM node.exe 2>nul
echo.

echo Step 5: Verifying dependencies...
call npx expo install --check
echo.

echo ========================================
echo   Done! Now run: npx expo start --clear
echo ========================================
pause











