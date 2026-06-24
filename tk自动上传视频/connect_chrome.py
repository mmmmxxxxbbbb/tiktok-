from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp("http://localhost:9222")

    # ⚠️ 必须用已有 context
    context = browser.contexts[0]

    # ⚠️ 用已有页面，而不是 new_page()
    page = context.pages[0] if context.pages else context.new_page()

    print("已接管真实Chrome")

    page.goto("https://www.tiktok.com/tiktokstudio/upload")

    input("按回车退出")