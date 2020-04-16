from flask import Blueprint,make_response,send_from_directory,request,jsonify,Flask
from data import cursor,db
import json
from datetime import datetime,date
import threading

lock = threading.Lock()


wz = Blueprint('wz', __name__)
app = Flask(__name__)


@wz.route("/dataAudio")          # 第一页数据的获取
def dataAudio():
    lock.acquire()
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit 10;")
    result = cursor.fetchall()
    lock.release()
    for i in result:
        if isinstance(i['upload_date'], (datetime, date)):
            i['upload_date'] = i['upload_date'].strftime('%Y-%m-%d')
    return json.dumps(result)


@wz.route("/dataLength")            # 获取节目数，进行分页
def dataLength():
    demo_dict = {}
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM wenzhao")
    result = cursor.fetchone()
    demo_dict["data_len"] = result['COUNT(*)']
    lock.release()
    return json.dumps(demo_dict)


@wz.route("/handleCurrentChange")       # 点击上一页、下一页
def handleCurrentChange():
    offset = int(request.args.get('offset'))
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit %s,10", offset)
    result = cursor.fetchall()
    for i in result:
        if isinstance(i['upload_date'], (datetime, date)):
            i['upload_date'] = i['upload_date'].strftime('%Y-%m-%d')
    return json.dumps(result)

