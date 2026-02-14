@echo off
echo ========================================
echo   Fix Windows Firewall for Backend
echo ========================================
echo.
echo This will create a firewall rule to allow
echo Python/Flask to accept connections on port 5000
echo.
echo Press any key to continue...
pause >nul

echo.
echo Creating firewall rule...
netsh advfirewall firewall add rule name="Flask Backend Port 5000" dir=in action=allow protocol=TCP localport=5000

if %errorlevel% equ 0 (
    echo.
    echo SUCCESS: Firewall rule created!
    echo.
    echo Now restart your backend:
    echo   1. Stop backend (Ctrl+C)
    echo   2. Start backend: cd backend ^&^& python app.py
    echo   3. Try login again in the app
) else (
    echo.
    echo ERROR: Could not create firewall rule
    echo You may need to run this as Administrator
    echo.
    echo Right-click this file and select "Run as administrator"
)

echo.
pause




