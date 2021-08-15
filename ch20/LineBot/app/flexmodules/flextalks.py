from linebot.models.send_messages import TextSendMessage
from app.flexmodules import flexmessages
from linebot.models import FlexSendMessage
from app import line_bot_api, handler
from app.dataSQL import connectDB

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
    query = event.postback.data
    print(query)
    if '=' in query:
        print(query.split('=')[1])
        data = connectDB.queryItem(query.split('=')[1])
        menu_name = [i[2] for i in data]
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text=f"query record: column {query}",
                contents= flexmessages.flex_menu_prize(query,menu_name)
            )
        )
        return True
    elif '菜單' in query:
        data = connectDB.showallMenu()
        menu_name = [i[1] for i in data]
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text=f"query record: column {query}",
                contents= flexmessages.flex_menu(query,menu_name)
            )
        )
        return True
    else:
        return False