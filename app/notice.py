import os
from dotenv import load_dotenv
import requests

# トークン読み込み
load_dotenv()

def send_line(screenshots_filename):
    try:
        # トークン
        token = os.getenv("TOKEN")
        # API
        api = "https://notify-api.line.me/api/notify"
        # 通知内容
        contents = f"ファイル名：{screenshots_filename}"

        token_dictionary = {"Authorization":f"Bearer {token}"}
        send_dictionary = {"message":contents}
        response_code = requests.post(api, headers= token_dictionary , data = send_dictionary)

        response_code.raise_for_status()
        print("送信成功")
    except Exception as e:
        print(f"エラー：{e}")