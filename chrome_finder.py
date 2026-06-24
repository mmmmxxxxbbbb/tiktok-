import os
import winreg

def get_chrome_path():

    # 常见安装路径
    paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
    ]

    for p in paths:
        if os.path.exists(p):
            return p

    # 注册表查找
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
        )
        value, _ = winreg.QueryValueEx(key, "")
        if os.path.exists(value):
            return value
    except:
        pass

    return None