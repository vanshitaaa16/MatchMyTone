@echo off
echo ========================================
echo   Complete Connection Fix
echo ========================================
echo.

echo Step 1: Checking backend status...
netstat -ano | findstr :5000
if %errorlevel% neq 0 (
    echo ERROR: Backend is NOT running on port 5000!
    echo Please start your backend first: cd backend ^&^& python app.py
    pause
    exit /b 1
)
echo OK: Backend is running
echo.

echo Step 2: Finding your IP address...
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4"') do (
    set IP=%%a
    set IP=!IP:~1!
    echo Found IP: !IP!
    goto :found
)
:found
echo.

echo Step 3: Testing backend connection...
echo Testing http://localhost:5000/api/health
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:5000/api/health' -UseBasicParsing -TimeoutSec 5; Write-Host 'SUCCESS: Backend is responding!'; Write-Host $response.Content } catch { Write-Host 'ERROR: Cannot connect to backend' }"
echo.

echo Step 4: Creating firewall rule...
netsh advfirewall firewall add rule name="Flask Backend Port 5000" dir=in action=allow protocol=TCP localport=5000 2>nul
if %errorlevel% equ 0 (
    echo SUCCESS: Firewall rule created/updated
) else (
    echo WARNING: Could not create firewall rule (may already exist or need admin)
)
echo.

echo ========================================
echo   IMPORTANT: Next Steps
echo ========================================
echo.
echo Your computer's IP address is: 192.168.31.111
echo.
echo If you're using Android EMULATOR:
echo   1. Make sure src/api.js uses: http://10.0.2.2:5000/api
echo   2. If 10.0.2.2 doesn't work, change to: http://192.168.31.111:5000/api
echo.
echo If you're using PHYSICAL Android device:
echo   1. Make sure src/api.js uses: http://192.168.31.111:5000/api
echo   2. Make sure your phone is on the SAME Wi-Fi network
echo.
echo After changing src/api.js:
echo   1. Save the file
echo   2. In Expo terminal, press 'r' to reload
echo   3. Or restart the app completely
echo.
echo ========================================
pause




