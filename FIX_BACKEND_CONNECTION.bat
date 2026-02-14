@echo off
echo ========================================
echo   Fixing Backend Connection Issue
echo ========================================
echo.
echo Your backend is running on: http://192.168.31.111:5000
echo But Expo Go cannot connect to it.
echo.
echo This is usually a Windows Firewall issue.
echo.
echo ========================================
echo   Solution: Allow Python through Firewall
echo ========================================
echo.
echo Opening Windows Firewall settings...
echo.
echo INSTRUCTIONS:
echo 1. Click "Allow an app or feature through Windows Defender Firewall"
echo 2. Click "Change settings" (if needed)
echo 3. Find "Python" in the list
echo 4. Check BOTH "Private" and "Public" boxes
echo 5. Click OK
echo.
echo OR create a rule for port 5000:
echo 1. Click "Advanced settings"
echo 2. Click "Inbound Rules" -^> "New Rule"
echo 3. Select "Port" -^> Next
echo 4. Select "TCP" and enter "5000"
echo 5. Select "Allow the connection"
echo 6. Check all profiles
echo 7. Name it "Flask Backend Port 5000"
echo 8. Click Finish
echo.
pause
start wf.msc











