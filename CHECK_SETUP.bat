@echo off
echo ========================================
echo   MatchMyTone - Setup Checker
echo ========================================
echo.

echo [1] Checking Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found! Please install Python 3.8+
    pause
    exit /b 1
)
echo OK: Python installed
echo.

echo [2] Checking Node.js...
node --version
if %errorlevel% neq 0 (
    echo ERROR: Node.js not found! Please install Node.js
    pause
    exit /b 1
)
echo OK: Node.js installed
echo.

echo [3] Checking Backend Dependencies...
cd backend
if not exist "requirements.txt" (
    echo ERROR: requirements.txt not found!
    pause
    exit /b 1
)
echo Checking if packages are installed...
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo WARNING: Backend dependencies not installed
    echo Run: pip install -r requirements.txt
) else (
    echo OK: Backend dependencies installed
)
cd ..
echo.

echo [4] Checking Frontend Dependencies...
if not exist "node_modules" (
    echo WARNING: node_modules not found
    echo Run: npm install
) else (
    echo OK: Frontend dependencies installed
)
echo.

echo [5] Checking Database Connection...
cd backend
python -c "import psycopg2; conn = psycopg2.connect('postgresql://postgres:postgres@localhost:5432/matchmytone'); print('OK: Database connection successful'); conn.close()" 2>nul
if %errorlevel% neq 0 (
    echo WARNING: Cannot connect to database
    echo Make sure PostgreSQL is running and database 'matchmytone' exists
    echo Default connection: postgresql://postgres:postgres@localhost:5432/matchmytone
) else (
    echo OK: Database connection successful
)
cd ..
echo.

echo ========================================
echo   Setup Check Complete!
echo ========================================
echo.
pause





