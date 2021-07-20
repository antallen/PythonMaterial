from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 靈活展現文字
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    # user id 在 Line Developers / Basic Setting 下
    if event.source.user_id == "user id":

        display_message = '你後面那位也想聽'

        if event.message.text == "tux來一個鬼故事":
            response_message = display_message

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_message)
        )
