from playwright.sync_api import sync_playwright
import os

os.makedirs("auth", exist_ok=True)

p = sync_playwright().start()

browser = p.chromium.launch(
    headless=False
)

context = browser.new_context()

page = context.new_page()

print("正在打开 TikTok...")

page.goto(
    "https://www.tiktok.com",
    timeout=60000
)

print("请登录 TikTok")

input("登录完成后按回车保存 Cookie：")

context.storage_state(
    path="auth/state.json"
)

print("登录状态保存成功！")

browser.close()
p.stop()