@echo off

echo 启动 Chrome Debug 模式...

start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
--remote-debugging-port=9222 ^
--user-data-dir="D:\chrome_debug"

timeout /t 3

echo 启动Python主程序...
python main.py

pause