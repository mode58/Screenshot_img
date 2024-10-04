from os import listdir
import time
import notice

def check_screenshot():
    global present_screenshot
    current_files = set(listdir(screenshot_dir)) #現在のファイル名を取得
    new_files = current_files - present_screenshot
    present_screenshot = current_files # 現在のファイル状況を適用
    return new_files

if __name__ == "__main__":
    screenshot_dir = "/path/to/screenshot/folder" # スクショフォルダのパス取得 ,後々Androidのパスに変更
    present_screenshot = set(listdir(screenshot_dir)) # 配下のファイル名全取得,差集合するので集合形式で保存
    while True:
        new_screenshots = check_screenshot()
        if new_screenshots: #空だったら処理しない
            notice.send_line(new_screenshots) # 通知を送信する処理
        time.sleep(5)  # 5秒ごとにチェック