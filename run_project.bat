@echo off
echo ====================================
echo   HICAS AI ASSISTANT - LAUNCHER
echo ====================================
echo.

cd /d "%~dp0"

:: 1. Check VENV
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup first.
    pause
    exit /b
)

:: 2. Activate VENV
echo [1/4] Activating Virtual Environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate venv.
    pause
    exit /b
)

:: 3. Kill existing python processes
echo [2/4] Cleaning up old processes...
taskkill /F /IM python.exe >nul 2>&1

:: 4. Start Backend
echo [3/4] Starting Backend Server...
start "HICAS Backend" cmd /k "venv\Scripts\activate.bat && cd backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

:: Wait for backend to init
timeout /t 5 /nobreak >nul

:: 5. Start Frontend
echo [4/4] Starting Frontend Server...
start "HICAS Frontend" cmd /k "venv\Scripts\activate.bat && cd frontend && python -m http.server 8080"

:: 6. Open Browser
echo.
echo Launching Browser...
start http://localhost:8080

echo.
echo ====================================
echo      APP RUNNING SUCCESSFULLY!
echo ====================================
echo.
echo Backend:  http://localhost:8000/docs
echo Frontend: http://localhost:8080
echo.
echo DO NOT CLOSE THE OPEN WINDOWS
echo.
pause
