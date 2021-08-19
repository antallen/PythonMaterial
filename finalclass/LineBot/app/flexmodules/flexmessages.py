# from linebot.models import FlexSendMessage
def fleximage(url):
    return { "type": "image",
             "url": url,
             "size": "full",
             "aspectRatio": "20:13",
             "aspectMode": "cover"}
             
def flextext(text,size,color,weight='regular',wrap=False):
    return { "type": "text",
             "text": text,
             "size": size,
             "color": color,
             "weight": weight,
             "wrap": wrap }
             
def flexlogo(text='大學麵店'):
    return flextext(text, size='md',color='#066BAF', weight='bold')

def flextitle(text):
    return flextext(text, size='xl',color='#066BAF', weight='bold')
    
def flexhead(text):
    return flextext(text, size='xl',color='#555555')
    
def flexnote(text):
    return flextext(text, size='md',color='#AAAAAA', wrap=True)
    
def flexseparator(margin='xl'):
    return { "type": "separator", "margin": margin }
    
def flexbutton(label, data, display_text):
    return { "type": "button",
             "action": {
                 "type": "postback",
                 "label": label,
                 "data": data,
                 "display_text": display_text },
                 "style": "link",
                 "color": "#066BAF",
                 "height": "sm" }
                 
def flex_index():
    hero_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png"
    bodys = [flexlogo(),
    		 flextitle('歡迎光臨'),
             flexseparator(),
             flexhead('菜單列表'),
             flexnote('# 列出所有菜單'),
             flexhead('單項查詢'),
             flexnote('# 查詢單項菜單'),
             flexseparator()]

    footers = [flexbutton('菜單列表','菜單','菜單列表'),
               flexbutton('單項查詢','單項','單項菜單查詢') ]

    FlexMessage = {'type': 'bubble',
                    'hero': fleximage(hero_url),
                    'body': {
                        'type': 'box',
                        'layout': 'vertical',
                        'spacing': 'md',
                        'contents': bodys},
                    'footer': {
                        'type': 'box',
                        'layout': 'vertical',
                        'contents': footers}}
    return FlexMessage
def flex_menu(keywords, data):
    hero_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png"
    bodys = [flexlogo(),
    		 flextitle(f'{keywords}'),
             flexseparator()]

    footers = [flexbutton(f"{i}",f"{keywords}={i}",f"查詢 {i}") for i in data]

    FlexMessage = { 'type': 'bubble',
                    'hero': fleximage(hero_url),
                    'body': {
                        'type': 'box',
                        'layout': 'vertical',
                        'spacing': 'md',
                        'contents': bodys},
                    'footer': {
                        'type': 'box',
                        'layout': 'vertical',
                        'contents': footers}}
    return FlexMessage

def flex_menu_prize(keywords, data):
    keyword = keywords.split('=')[1]
    hero_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png"
    bodys = [flexlogo(),
    		 flextitle(f'{keyword}'),
             flexseparator(),
             flexnote(f'價格:{data}'),
             flexseparator()]

    footers = [flexbutton("菜單查詢","菜單查詢","菜單列表")]

    FlexMessage = { 'type': 'bubble',
                    'hero': fleximage(hero_url),
                    'body': {
                        'type': 'box',
                        'layout': 'vertical',
                        'spacing': 'md',
                        'contents': bodys},
                    'footer': {
                        'type': 'box',
                        'layout': 'vertical',
                        'contents': footers}}
    return FlexMessage