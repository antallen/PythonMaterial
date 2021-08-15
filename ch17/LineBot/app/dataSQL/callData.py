from app import line_bot_api
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, messages
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn, URIAction
from app.dataSQL import connectDB

def showData(event):

    if '新增菜單' in event.message.text:
        input_str = event.message.text
        manu = input_str.split(':')
        data = connectDB.addMenu(manu[1])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='新增成功！')
        )
        return True
    elif '菜單' in event.message.text:
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