from app import line_bot_api
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, messages
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn, URIAction
from app.dataSQL import connectDB

import random

def showData(event):
    if '菜單' in event.message.text:
        data = connectDB.showallMenu()
        print_text = ""
        for i in data:
            print_text += str(i[1])
            print_text += str(i[2])
            print_text += "\n"

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=print_text)
        )

        return True
    else:
        return False