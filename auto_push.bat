@echo off

cd /d D:\Aayush_Sankhla_Internship

git add .

git diff --cached --quiet
if %errorlevel%==0 (
    echo No changes to commit
    pause
    exit
)

git commit -m "Daily update"

git push origin main

pause