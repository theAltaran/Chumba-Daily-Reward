@echo off

if not exist .env (
    :waitForInput
    choice /C YN /M "The .env file was not found. Would you like to run setup.bat?"
    if errorlevel 2 goto :eof
    if errorlevel 1 goto runSetup
    goto waitForInput

    :runSetup
    echo Running get_password.py...
    python get_password.py

    echo.
    echo Installing dependencies...
    pip install -r requirements.txt

    echo.
    echo Setup complete.

    echo Marking setup as completed...
    echo > setup_completed.marker
    goto runMain
)

:runMain
echo Running main.py...
python main.py

echo.
echo Setup complete.

echo Marking setup as completed...
echo > setup_completed.marker
