from linebot.models import ImageSendMessage
from app import line_bot_api, handler
import re
import urllib.request
import random

def istockSearch(event):

    try:

        search_key_word = {'family': 'creative', 'phrase': event.message.text}
        url = f"https://www.istockphoto.com/search/2/image?{urllib.parse.urlencode(search_key_word)}"
        header = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0' }
        req = urllib.request.Request(url, headers=header)
        conn = urllib.request.urlopen(req)
        data = conn.read()
        template = 'src="(https://media.*?)"'
        image_list = []
            
        for i in re.finditer(template,str(data,'utf-8')):
            image_list.append(re.sub('amp;', '', i.group(1)))

        random_image_url = image_list[random.randint(0, len(image_list)+1)]

        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=random_image_url,
                preview_image_url=random_image_url
            )
        )

        return True
    except:
        return False
