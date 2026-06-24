# TikTok Auto Uploader

## English

A simple TikTok batch uploader built with Playwright.

The project connects to an already logged-in Chrome browser through Chrome Remote Debugging Protocol (CDP), allowing automated uploads to TikTok Studio.

### Features

- Batch upload TikTok videos
- Connect to existing Chrome session
- Random titles and hashtags
- Multiple content categories
- Custom upload interval
- Automatic video classification
- Easy to extend

---

## Supported Categories

Current examples:

- toy_my
- beauty_tiktok

You can easily add your own categories.

---

## Project Structure

```text
.
├── chrome_finder.py
├── connect_chrome.py
├── config.py
├── login.py
├── main.py
├── uploader.py
├── rename_videos.py
│
├── titles/
│   ├── toy_my.txt
│   └── beauty_tiktok.txt
│
├── tags/
│   ├── toy_my.txt
│   └── beauty_tiktok.txt
│
├── videos/
│   ├── toy_my/
│   └── beauty_tiktok/
│
├── start.bat
├── run.bat
└── cmd.bat
```

---

## Installation

### 1. Clone Project

```bash
git clone https://github.com/YOUR_USERNAME/TikTokAutoUploader.git
cd TikTokAutoUploader
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## Chrome Setup

Close all Chrome windows.

Start Chrome with Remote Debugging:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="chrome_profile"
```

Login to TikTok inside this browser.

Open:

```text
https://www.tiktok.com/tiktokstudio/upload
```

---

## Run

```bash
python main.py
```

Choose upload category:

```text
1. toy_my
2. beauty_tiktok
3. all
```

---

## Video Folder Structure

```text
videos/
├── toy_my/
│   ├── 001.mp4
│   ├── 002.mp4
│   └── ...
│
└── beauty_tiktok/
    ├── 001.mp4
    ├── 002.mp4
    └── ...
```

---

## Title Files

Example:

```text
titles/toy_my.txt
```

```text
Best water gun ever 🔥
Summer toy fun ☀️
Perfect outdoor game 🎯
```

---

## Tag Files

Example:

```text
tags/toy_my.txt
```

```text
#watergun #summerfun #toys
#toyreview #kidsfun #outdoorplay
```

---

## Disclaimer

This project is for educational purposes only.

Users are responsible for complying with TikTok's Terms of Service and all applicable laws.

---

# 中文说明

一个基于 Playwright 的 TikTok 自动上传工具。

通过连接已经登录的 Chrome 浏览器，实现 TikTok Studio 自动上传。

---

## 功能特点

- TikTok 批量上传
- 自动连接已登录 Chrome
- 随机标题
- 随机标签
- 多分类管理
- 自定义上传间隔
- 自动识别视频分类
- 可扩展内容库

---

## 安装依赖

安装 Python 3.10+

执行：

```bash
pip install -r requirements.txt
playwright install
```

---

## 启动 Chrome 调试模式

关闭所有 Chrome。

运行：

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="chrome_profile"
```

登录 TikTok。

打开：

```text
https://www.tiktok.com/tiktokstudio/upload
```

---

## 运行程序

```bash
python main.py
```

根据提示选择：

```text
1. 玩具
2. 美妆
3. 全部
```

即可开始自动上传。

---

