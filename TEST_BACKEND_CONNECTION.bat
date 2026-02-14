@echo off
echo ========================================
echo   Testing Backend Connection
echo ========================================
echo.

echo [1] Testing localhost connection...
curl http://localhost:5000/api/health
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Cannot connect to backend on localhost:5000
    echo Make sure backend is running!
    pause
    exit /b 1
)
echo.
echo.

echo [2] Checking if port 5000 is listening...
netstat -ano | findstr :5000
echo.

echo [3] Finding your IP address...
ipconfig | findstr /i "IPv4"
echo.

echo ========================================
echo   Connection Test Complete
echo ========================================
echo.
echo If localhost test worked but app still fails:
echo - Check Windows Firewall settings
echo - For Android emulator, make sure you're using 10.0.2.2
echo - For physical device, use your computer's IP address
echo.
pause




