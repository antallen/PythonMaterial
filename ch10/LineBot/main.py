import os
from typing import Text
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
import configparser

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 導入 config.ini 檔案
config = configparser.ConfigParser()
config.read('config.ini')

# Line 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('LineBot','channel_access_toke'))
handler = WebhookHandler(config.get('LineBot','channel_secret'))

# 接收 line 平台送來的「通知」
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 鸚鵡學說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):

    # user id 在 Line Developers / Basic Setting 下
    if event.source.user_id == "user id":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

## 程式進入點
if __name__ == "__main__":
    app.run()
