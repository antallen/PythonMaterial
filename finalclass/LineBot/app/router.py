import re

from werkzeug.utils import html
from app import app, handler, request, abort
from linebot.exceptions import InvalidSignatureError
from app.dataSQL import connectDB
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.loginmodels import User, users_dict

@app.route('/logins', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    user = request.form['loginname']
    print(user)
    conditionA = user in users_dict
    conditionB = request.form['password'] == users_dict[user]['password']

    if conditionA and conditionB:
        user1 = User()
        user1.id = user
        login_user(user1)
        flash(f'{user}!Welcome home!')
        return redirect(url_for('home'))

    flash('login failed...')
    return render_template('login.html')

@app.route('/logout')
def logout():
    user = current_user.get_id()
    logout_user()
    flash(f'{user}!logout!')
    return render_template('login.html')

@app.route('/show_records')
@login_required
def show_records():
    python_records =web_select_overall()
    return render_template('show_records.html', html_records=python_records)

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