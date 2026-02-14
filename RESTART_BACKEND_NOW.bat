@echo off
echo ========================================
echo   Restarting Backend Server
echo ========================================
echo.
echo Step 1: Stopping any existing Python processes...
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul
echo.
echo Step 2: Starting backend server...
cd backend
python app.py
pause











