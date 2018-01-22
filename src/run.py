from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
import json
from control_mongo import *

app = Flask(__name__,static_url_path='')
app.config['SECRET_KEY'] = "123"

@app.route('/')
def index():
    return render_template('index2.html', title='116')

@app.route('/login01', methods=[ 'GET','POST'])
def Login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    e = Select(username, password)
    if e == "OK":
        print("OK")
        d = {"get": "OK"}
        return jsonify(d)
        #return render_template('login_ok.html')  # 如果验证成功返回一个页面（可以设置为用户的使用界面）
    else:
        print("NO")
        f = {"username": username, "password": password, "get": "NO"}
        return jsonify(f)

@app.route('/signup01', methods=[ 'GET','POST'])
def SignUp():
    test = request.form['usernamesignup']
    #test = request.values["mydata"]
    print(test)
    a = SelectName(test)
    print(a)
    if a == "OK":
        b = {"g": 'OK'}
        return jsonify(b)
    else:
        c = {"g": 'NO'}
        return jsonify(c)





@app.route('/myformLogin', methods=[ 'GET', 'POST'])
def myformLogin():
    print('post')
    username = request.form['username']
    password = request.form["password"]
    print(username)
    print(password)
    e = Select(username,password)
    if e == "OK":
        print("OK")
        #d = {"OK":"success"}
        return render_template('login_ok.html') #如果验证成功返回一个页面（可以设置为用户的使用界面）
    else:
    #     print("NO")
         d = {"username":username,"password":password}
    #     return render_template('login_no_1.html')  #显示一个错误网页 找不到用户名
         return jsonify(d)

@app.route('/myformSignUp', methods=[ 'POST'])
def myformSignUp():
    usernamesignup = request.form['usernamesignup']
    emailsignup = request.form['emailsignup']
    passwordsignup = request.form["passwordsignup"]
    passwordsignup_confirm = request.form["passwordsignup_confirm"]
    qqsignup = request.form['qqsignup']
    telsignup = request.form['telsignup']
    agesignup = request.form['agesignup']
    addresssignup = request.form['addresssignup']
    #add(usernamesignup ,passwordsignup ,emailsignup , qqsignup, telsignup, agesignup ,addresssignup)
    print("add ok")
    a = SelectName(usernamesignup)  #检查用户名是否存在，因为我们已经把name（用户名），设定为唯一约束
    if a == "NO":    # SelectName返回 NO 说明之前并不存在输入的用户名
        add(usernamesignup, passwordsignup, emailsignup, qqsignup, telsignup, agesignup, addresssignup)
        d = {"usernamesignup":usernamesignup , "passwordsignup":passwordsignup_confirm}
        #return jsonify(d)
        return render_template('index2.html')  # 如果验证成功返回一个页面（可以设置为用户的登陆界面）

    else:
        e = {"usernamesignup":"have one"}
        return jsonify(e)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7777, debug=True)

    # host：主机，在使用run()启动服务的时候指定的IP地址，默认情况下是127.0.0.1
    # port：端口，是run()启动服务的时候指定的运行端口，默认是5000
    # debug：调试，如果需要进入调试模式，可以将这个选项设置成ture
    # options: 选项参数是将server的参数传送到Werkzeugserver去处理。详情参考链接内容

