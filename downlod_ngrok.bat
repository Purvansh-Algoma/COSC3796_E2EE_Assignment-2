@echo off
echo Downloading ngrok for your assignment...
echo.
echo Step 1: Downloading ngrok.zip...
powershell -Command "Invoke-WebRequest -Uri 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip' -OutFile 'ngrok.zip'"

echo.
echo Step 2: Extracting ngrok.exe...
powershell -Command "Expand-Archive -Path 'ngrok.zip' -DestinationPath '.'"

echo.
echo Step 3: Cleaning up...
del ngrok.zip

echo.
echo ✅ Ngrok downloaded successfully!
echo Run it with: ngrok.exe http 5000
pause