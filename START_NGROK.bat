@echo off
echo ========================================
echo   Starting ngrok Tunnel
echo ========================================
echo.
echo This will create a public URL for your backend
echo that works from anywhere, bypassing firewalls!
echo.
echo Make sure ngrok.exe is in this folder or update the path below.
echo.
pause

REM Update this path to where your ngrok.exe is located
cd /d "%~dp0"
ngrok http 5000

pause




