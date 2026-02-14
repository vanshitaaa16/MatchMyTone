@echo off
echo ========================================
echo   Fixing Expo Go Connection Issue
echo ========================================
echo.
echo The error "Failed to download remote update" means
echo Expo Go cannot connect to Metro bundler.
echo.
echo Solutions:
echo.
echo 1. Make sure phone and computer are on SAME Wi-Fi
echo 2. Try tunnel mode (press 's' in Expo terminal)
echo 3. Check Windows Firewall
echo.
echo ========================================
echo.
echo Starting Expo with TUNNEL mode...
echo (This will work even if firewall blocks LAN)
echo.
pause
npx expo start --tunnel --clear











