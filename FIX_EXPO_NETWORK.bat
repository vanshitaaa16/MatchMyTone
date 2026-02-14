@echo off
echo Fixing Expo network error...
echo.

echo Step 1: Clearing Expo cache...
npx expo start --clear

if %errorlevel% neq 0 (
    echo.
    echo Trying offline mode...
    npx expo start --offline
)



