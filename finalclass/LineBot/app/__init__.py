from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
import configparser
from flask_login import LoginManager

app = Flask(__name__)

# 導入 config.ini 檔案
config = configparser.ConfigParser()
config.read('config.ini')

# Line 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('LineBot','channel_access_token'))
handler = WebhookHandler(config.get('LineBot','channel_secret'))

# 導入加密 key
app.secret_key = config.get('Flask','SecretKey')

lm = LoginManager()
lm.init_app(app)
lm.session_protection = "strong"
lm.login_view = 'login'
lm.login_message = '請輸入帳號密碼'


# 導入其他的程式模組
from app import router, linebotmodules, loginmodels