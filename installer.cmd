@echo off
setlocal enabledelayedexpansion

:ask1
echo Do you really want to install FMOS? [Y/N]
set /p input=
if /i "%input%"=="Y" goto install
if /i "%input%"=="N" goto dontinstall
goto ask1

:install
mkdir "C:\FMOS"
mkdir "C:\FMOS\System"
mkdir "C:\FMOS\System\sys"
mkdir "C:\FMOS\System\boot"
mkdir "C:\FMOS\System\security"
mkdir "C:\FMOS\System\temp"
mkdir "C:\FMOS\System\trash"
mkdir "C:\FMOS\Programms"
mkdir "C:\FMOS\Programms\sys"
mkdir "C:\FMOS\Programms\fak"
mkdir "C:\FMOS\usr"
mkdir "C:\FMOS\usr\Desktop"
mkdir "C:\FMOS\usr\Downloads"
mkdir "C:\FMOS\usr\Docs"
echo Done creating folders
echo.

echo Choose a Username:
set /p chname=
echo %chname% > "C:\FMOS\System\sys\usr"
echo.

:ask2
cls
echo Do you want to have Root (admin) permissions on FMOS? [Y/N]
set /p ask2=
if /i "%ask2%"=="Y" goto root
if /i "%ask2%"=="N" goto dontroot
goto ask2

:root
mkdir "C:\FMOS\System\security\root"
echo. > "C:\FMOS\System\security\root\rootuser"
echo.

echo Choose a Password for Root:
set /p rootpass=
set "python_script=import base64; import sys; print(base64.b64encode(sys.argv[1].encode()).decode())"
for /f "delims=" %%i in ('python -c "%python_script%" "%rootpass%"') do set "encoded_text=%%i"
echo !encoded_text!
echo !encoded_text! > "C:\FMOS\System\security\rootpass.md"
goto dontroot

:dontroot
python -c "import requests; urls = [('https://fabischau1.github.io/FMOS_Python/README.md', 'C:\\FMOS\\usr\\README.md'), ('https://fabischau1.github.io/FMOS_Python/boot.bat', 'C:\\FMOS\\System\\boot\\boot.bat'), ('https://fabischau1.github.io/FMOS_Python/boot.py', 'C:\\FMOS\\System\\boot\\boot.py'), ('https://fabischau1.github.io/FMOS_Python/main.py', 'C:\\FMOS\\System\\sys\\main.py'), ('https://fabischau1.github.io/FMOS_Python/main.cmd', 'C:\\FMOS\\System\\sys\\main.cmd')]; import requests; [open(dest, 'wb').write(requests.get(url).content) for url, dest in urls]"

pip install requests
pip install keyboard
echo Installation finished
echo Press any key to boot FMOS
pause
call "C:\FMOS\System\boot\boot.bat"

:dontinstall
exit
