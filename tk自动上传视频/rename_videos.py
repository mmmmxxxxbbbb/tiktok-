import os

VIDEO_FOLDERS = [
    r"D:\代码相关\videos\toy_my",
    r"D:\代码相关\videos\beauty_tiktok"
]


def rename_folder(folder_path):

    if not os.path.exists(folder_path):
        print("路径不存在:", folder_path)
        return

    files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]
    files.sort()

    if not files:
        print("没有视频:", folder_path)
        return

    print(f"\n===== 处理文件夹: {folder_path} =====")

    # 第一步：改成临时名，避免冲突
    temp_names = []

    for i, f in enumerate(files):
        old_path = os.path.join(folder_path, f)
        temp_path = os.path.join(folder_path, f"temp_{i}.mp4")
        os.rename(old_path, temp_path)
        temp_names.append(temp_path)

    # 第二步：按顺序重命名
    for i, temp_path in enumerate(temp_names, start=1):
        new_name = f"{i:03d}.mp4"
        new_path = os.path.join(folder_path, new_name)

        os.rename(temp_path, new_path)
        print(f"{os.path.basename(temp_path)} → {new_name}")

    print("完成:", folder_path)


def run():

    for folder in VIDEO_FOLDERS:
        rename_folder(folder)


if __name__ == "__main__":
    run()