@echo off
echo ========================================
echo   MatchMyTone - Complete Startup
echo ========================================
echo.

echo [1/3] Starting Backend Server...
cd backend
start "Backend Server" cmd /k "python app.py"
timeout /t 3 /nobreak >nul

echo.
echo [2/3] Backend should be running on http://localhost:5000
echo       Check the Backend Server window to confirm
echo.

echo [3/3] Starting Expo Development Server...
cd ..
start "Expo Dev Server" cmd /k "npm start"

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Backend: http://localhost:5000
echo Expo: Check the Expo Dev Server window
echo.
echo Press any key to exit...
pause >nul





