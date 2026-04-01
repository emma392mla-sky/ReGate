@echo off
cd /d "C:\Users\DELL\Desktop\python projects"

for /f "tokens=2-6" %%a in ('curl -sI https://google.com ^| findstr /i "Date:"') do set "dt=%%a %%b %%c %%d %%e"

git add .
git commit -m "Updated %dt%"
git push origin main

git mv dockerfile Dockerfile
git commit -m "Fix Dockerfile naming"
git push origin main

pause