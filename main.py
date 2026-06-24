import os
import random
import time
from playwright.sync_api import sync_playwright

from uploader import upload_video
from config import CONTENT_MAP, random_delay

VIDEO_ROOT = r"D:\代码相关\videos"


# 📌 随机文本
def load_random(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    return random.choice(lines)


# 📌 获取所有视频
def get_videos():
    videos = []
    for root, _, files in os.walk(VIDEO_ROOT):
        for f in files:
            if f.endswith(".mp4"):
                videos.append(os.path.join(root, f))
    return sorted(videos)


# 📌 自动识别类型
def detect_type(video_path):
    if "toy_my" in video_path:
        return "toy_my"
    if "beauty_tiktok" in video_path:
        return "beauty_tiktok"
    return None


# 📌 选择投放类型
def choose_category():
    print("\n===== 选择投放类型 =====")
    print("1. toy_my（玩具）")
    print("2. beauty_tiktok（美妆）")
    print("3. all（全部）")

    choice = input("请输入：")

    if choice == "1":
        return ["toy_my"]
    elif choice == "2":
        return ["beauty_tiktok"]
    else:
        return ["toy_my", "beauty_tiktok"]


def run():

    selected_types = choose_category()

    with sync_playwright() as p:

        # 🚀 连接真实Chrome（CDP）
        browser = p.chromium.connect_over_cdp("http://localhost:9222")

        context = browser.contexts[0]
        page = context.pages[0] if context.pages else context.new_page()

        print("已接管Chrome")

        page.goto("https://www.tiktok.com/tiktokstudio/upload")

        # 📦 获取视频并过滤
        videos = get_videos()

        videos = [
            v for v in videos
            if detect_type(v) in selected_types
        ]

        if not videos:
            print("没有符合条件的视频")
            return

        # 🔥 批量上传
        for v in videos:

            vtype = detect_type(v)

            title = load_random(CONTENT_MAP[vtype]["title"])
            tag = load_random(CONTENT_MAP[vtype]["tag"])

            print(f"\n===== 上传 {v} =====")
            print("类型:", vtype)

            upload_video(page, v, title, tag)

            delay = random_delay(vtype)
            print(f"等待 {delay} 秒...")
            time.sleep(delay)

        print("全部完成")


if __name__ == "__main__":
    run()