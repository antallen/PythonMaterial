from linebot.models.send_messages import TextSendMessage
from app.flexmodules import flexmessages
from linebot.models import FlexSendMessage
from app import line_bot_api, handler
from app.dataSQL import callData

def query_menu(event):
    if '菜單查詢' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='query record: index',contents=flexmessages.flex_index())
        )
        return True
    else:
        return False

def query_menu_back(event):
    callData.showData(event)