@echo off

:: Run the Python script
python ./dev.py

:: Display the current status of the repository
git status

:: Stage all changes
git add .

:: Ask for a commit message
set /p commitMessage=Enter commit message: 

:: Commit the changes with the provided message
git commit -m "%commitMessage%"

:: Push changes to the main branch
git push origin main

:: Check if the push was successful
if %errorlevel% neq 0 (
    echo Push failed! Please check the error message.
    pause
    exit /b 1
)

:: Pause to keep the terminal open for review
pause
