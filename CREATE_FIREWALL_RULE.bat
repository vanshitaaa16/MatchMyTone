@echo off
echo ========================================
echo   Creating Firewall Rule for Port 5000
echo ========================================
echo.
echo This will create a firewall rule to allow
echo connections to port 5000 from any network.
echo.
pause

netsh advfirewall firewall add rule name="Flask Backend Port 5000" dir=in action=allow protocol=TCP localport=5000 profile=domain,private,public

echo.
echo ========================================
echo   Rule Created!
echo ========================================
echo.
echo The rule has been created for:
echo - Domain networks
echo - Private networks  
echo - Public networks (important for phones!)
echo.
echo Now test from your phone:
echo http://192.168.31.111:5000/api/health
echo.
pause




