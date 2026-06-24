from playwright.sync_api import TimeoutError


def upload_video(page, video_path, title, tag):

    print("上传:", video_path)

    try:
        page.wait_for_load_state("domcontentloaded")

        # ===== 1. 上传视频 =====
        print("选择文件...")

        file_input = page.locator('input[type="file"]')
        file_input.wait_for(state="attached", timeout=120000)

        file_input.set_input_files(video_path, timeout=120000)

        page.wait_for_timeout(5000)

        # ===== 2. 填标题 =====
        print("填写标题")

        title_box = page.locator('div[contenteditable="true"]').first
        title_box.click()
        title_box.fill(title)

        # ===== 3. 填 tag =====
        print("填写tag")
        page.keyboard.type(" " + tag)

        page.wait_for_timeout(3000)

        # ===== 4. 点击发布 =====
        print("点击发布")

        post_btn = page.locator('button[data-e2e="post_video_button"]')
        post_btn.wait_for(timeout=120000)
        post_btn.click()

        page.wait_for_timeout(5000)

        # ===== 5. 弹窗处理 =====
        popup = page.locator(
            'button:has-text("Post now"), '
            'button:has-text("Continue"), '
            'button:has-text("Confirm"), '
            'button:has-text("OK")'
        )

        if popup.first.is_visible():
            print("处理弹窗...")
            popup.first.click()
            page.wait_for_timeout(3000)

        # ===== 6. 等待稳定 =====
        page.wait_for_timeout(5000)

        # ===== 7. 强制回到上传页（关键） =====
        print("返回上传页面...")

        page.goto(
            "https://www.tiktok.com/tiktokstudio/upload",
            wait_until="domcontentloaded"
        )

        page.wait_for_timeout(5000)

        print("发布完成")

    except TimeoutError:
        print("上传超时，尝试刷新页面恢复状态...")
        page.reload()
        page.wait_for_timeout(5000)