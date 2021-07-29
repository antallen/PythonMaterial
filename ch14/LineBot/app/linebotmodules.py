from linebot.models.send_messages import ImageSendMessage
from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import URIAction
import urllib.request
import re
import random
from app.dataSQL import callData

# 到 google 上找尋圖片的程式
def google_search(target):
    search_key_word = {'tbm': 'isch', 'q': target, 'client': 'firefox-b-e','source': 'lnms'}
    url = f"https://www.google.com/search?{urllib.parse.urlencode(search_key_word)}/"
    header = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' }
    req = urllib.request.Request(url, headers=header)
    conn = urllib.request.urlopen(req)
    data = conn.read()
    template = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
    image_list = []
    for i in re.finditer(template,str(data,'utf-8')):
        image_list.append(re.sub(r'\\u003d','=',i.group(1)))

    return image_list[random.randint(0, len(image_list)+1)]

def echo(messages):
    # user id 在 Line Developers / Basic Setting 下
    display_message = '你後面那位也想聽'
    if messages == "tux來一個鬼故事":
        response_message = display_message
    else:
        response_message = "不知道你在講什麼"
    return response_message 

# 靈活展現文字
@handler.add(MessageEvent, message=TextMessage)
def replyText(event):
    if event.source.user_id == "Uf4a596a6eb65eabf52c003ffe325a21d":
       reply = False
       if not reply:
           reply = callData.showData(event)

      # try:
      #     img_url = google_search(event.message.text)
      #     print(img_url)
      #     line_bot_api.reply_message(
      #         event.reply_token,
      #         ImageSendMessage(
      #             original_content_url=img_url,
      #             preview_image_url=img_url
      #         )
      #     )
           
      # except:
          #hello_text = echo(event.message.text)
      #    line_bot_api.push_message(
      #      'Uf4a596a6eb65eabf52c003ffe325a21d',
      #      TextSendMessage(text='沒找到')
      #    )
