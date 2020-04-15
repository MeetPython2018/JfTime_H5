from flask import Flask,render_template,request,redirect,session,make_response,send_from_directory,jsonify,Response
import math
import os
from data import cursor,db
from datetime import timedelta
# from flask_session import Session
from werkzeug.utils import secure_filename
import time
import json
import hashlib
import threading

lock = threading.Lock()

from url.jftime import jftime
from url.wz import wz


app = Flask(__name__)
app.register_blueprint(jftime,url_prefix='/ajax/jftime')
app.register_blueprint(wz,url_prefix='/ajax/wz')

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)


@app.route("/")
def home():
    res = make_response(render_template("index.html"))
    return res


@app.route("/ajax/sign_up")     # 注册逻辑
def sign_up():
    userName = request.args.get('userName')
    password = request.args.get('password')
    lock.acquire()
    cursor.execute("SELECT * FROM users where username = %s",userName)
    lock.release()
    result = cursor.fetchall()
    md5 = hashlib.md5()
    demo_md5 = password.encode(encoding='utf-8')
    md5.update(demo_md5)
    pass_md5 = md5.hexdigest()
    if(len(result) == 0 ):
        cursor.execute("Insert into users (username,password) values(%s,%s)",(userName,pass_md5))
        db.commit()
        sign_up = [{"sign_up": 200}]
    else:
        sign_up = [{"sign_up": 400}]
    return json.dumps(sign_up)


@app.route("/ajax/sign_in", methods=['POST'])     # 登录逻辑
def sign_in():
    userName = request.form['userName']
    password = request.form['password']
    md5 = hashlib.md5()
    demo_md5 = password.encode(encoding='utf-8')
    md5.update(demo_md5)
    pass_md5 = md5.hexdigest()
    lock.acquire()
    cursor.execute("SELECT * FROM users where username = %s and password = %s",(userName,pass_md5))
    lock.release()
    result = cursor.fetchall()
    if(result):
        sign_in = {"sign_in":200}
        session['login'] = 'ok'
        session['userName'] = userName
        session['pass_md5'] = pass_md5
    else:
        sign_in = {"sign_in":400}
    return json.dumps(sign_in)


@app.route("/ajax/get_sessions")
def get_sessions():
    ss = {"sessions":session.get('login')}
    return json.dumps(ss)


@app.route("/ajax/sign_out")
def sign_out():
    session.pop('login',None)
    return json.dumps({'sign_out':'ok'})


@app.route("/ajax/seeMessages")
def seeMessages():
    id = request.args.get('audio_id')
    lock.acquire()
    cursor.execute('Select * from comment where audio=%s',id)
    lock.release()
    result = cursor.fetchall()
    return json.dumps(result)


@app.route("/ajax/comment", methods=['POST'])
def comment():
    session.pop('login', None)
    user = request.form['user']
    audio_id = request.form['audio_id']
    comments = request.form['comment']
    time_stamp = request.form['time_stamp']
    lock.acquire()
    cursor.execute("Insert into comment (content,users,audio,comment_time) values(%s,%s,%s,%s)",(comments,user,audio_id,time_stamp))
    db.commit()
    lock.release()
    return json.dumps({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)