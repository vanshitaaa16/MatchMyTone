@echo off
echo Testing backend connectivity...
echo.

echo Test 1: Testing localhost...
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://localhost:5000/api/health' -UseBasicParsing -TimeoutSec 5; Write-Host 'SUCCESS - Localhost works'; Write-Host $r.Content } catch { Write-Host 'FAILED - Localhost:' $_.Exception.Message }"

echo.
echo Test 2: Testing 10.0.2.2 (Android emulator IP)...
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://10.0.2.2:5000/api/health' -UseBasicParsing -TimeoutSec 5; Write-Host 'SUCCESS - 10.0.2.2 works'; Write-Host $r.Content } catch { Write-Host 'FAILED - 10.0.2.2:' $_.Exception.Message }"

echo.
echo Test 3: Testing network IP 192.168.25.205...
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://192.168.25.205:5000/api/health' -UseBasicParsing -TimeoutSec 5; Write-Host 'SUCCESS - Network IP works'; Write-Host $r.Content } catch { Write-Host 'FAILED - Network IP:' $_.Exception.Message }"

echo.
pause


