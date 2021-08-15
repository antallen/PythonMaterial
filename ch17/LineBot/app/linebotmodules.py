from linebot.models.events import Postback, PostbackEvent
from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.send_messages import ImageSendMessage
from linebot.models import PostbackEvent

from app.dataSQL import callData
from app.picSearch import istock
from app.flexmodules import flextalks

# 訊息轉送站
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    # user id 在 Line Developers / Basic Setting 下
    if event.source.user_id == "Uf4a596a6eb65eabf52c003ffe325a21d":

        replay = False

        if not replay:
            reply = flextalks.query_menu(event)

        if not replay:
            reply = callData.showData(event)
        
        if not replay:
            replay = istock.istockSearch(event)

        if not replay:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )

# line 回應的訊息
@handler.add(PostbackEvent)
def handle_postback(event):
    print(event)
    flextalks.query_menu_back(event)
