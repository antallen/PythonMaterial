from app import app, handler, request, abort
from linebot.exceptions import InvalidSignatureError
from flask import render_template

# 設定預設網頁
@app.route("/")
def home():
    return render_template("home.html")

# 接收 Line 平台來的「通知」
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 導向查詢菜單內容的網頁
app.route("/showmenu")
def showmenu():
    return render_template("menu.html")