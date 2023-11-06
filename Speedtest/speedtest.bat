@echo off
set logfile="C:\Users\tlilly\Documents\Speedtest\speedtest.txt"
echo. >> %logfile%
echo %date% %time% >> %logfile%
speedtest.exe >> %logfile%
