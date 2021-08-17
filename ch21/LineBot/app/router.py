import re
from app import app, handler, request, abort
from linebot.exceptions import InvalidSignatureError
from flask import render_template
from app.dataSQL import connectDB

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

# 顯示菜單清單列表
@app.route("/showmenu")
def showmenu():
    menulists = connectDB.showallMenu()
    return render_template('menu.html',menulist=menulists)

# 新增菜單功能
@app.route("/addmenu",methods=['GET','POST'])
def addmenu():
    if request.method == 'POST':
        print(request.form)
        data = ""
        for key,value in request.form.items():
            data += value
            data += ','
        data = data[:-1]
        connectDB.addMenu(data)
        return showmenu()
    else:
        return render_template("addmenu.html")

# 刪除菜單資料
@app.route("/delmenu",methods=['GET','POST'])
def delmenu():
    if request.method == 'POST':
        print(request.form)
        data = ""
        data1 = ""
        for key, value in request.form.items():
            data = eval(''.join(value))
            data1 = str(data[0])+','+str(data[1])
            print(data1)
            connectDB.deleteMenu(data1)
        return showmenu()
    else:
        return render_template("menu.html")

# 顯示活動清單列表
@app.route("/showads")
def showads():
    adslists = connectDB.showAds()
    return render_template('showads.html',menulist=adslists)

# 新增活動清單
@app.route("/addads",methods = ['GET','POST'])
def addads():
    if request.method == 'POST':
        print(request.form)
        return showads()
    else:
        return render_template("addads.html")
# 刪除活動清單
@app.route("/delads",methods = ['GET','POST'])
def delads():
    if request.method == 'POST':
        print(request.form)
        data = ""
        data1 = ""
        for key, value in request.form.items():
            data = eval(''.join(value))
            data1 = str(data[0])+','+str(data[1])
            print(data1)
            connectDB.deleteAds(data1)
        return showads()
    else:
        return render_template("showads.html")

@app.route('/orderMenu/<nodes>')
def orders(nodes):
    return render_template("orderMenu.html",nodeslist=nodes)

@app.route('/orderMenu',methods = ['GET','POST'])
def addorders():
    if request.method == 'POST':
      print(request.form)
      data = ""
      for key,value in request.form.items():
          data += value
          data += ','
      data = data[:-1]
      connectDB.addOrders(data)
      return render_template("showOrders.html")
    else:
      return render_template("showOrders.html")

# 顯示訂單列表
@app.route("/showOrders")
def showOrders():
    orderslists = connectDB.showOrders()
    return render_template('showOrders.html',menulist=orderslists)