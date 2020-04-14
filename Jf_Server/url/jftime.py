from flask import Blueprint,make_response,send_from_directory,request,jsonify,Flask,session
from data import cursor,db
import json
import threading

lock = threading.Lock()


jftime = Blueprint('jftime', __name__)
app = Flask(__name__)


@jftime.route("/pullAudios")
def pullAudios():
    first_page_data = []
    lock.acquire()
    cursor.execute("Select * FROM jfmt order by `index` desc limit 5")
    lock.release()
    result1 = cursor.fetchall()
    first_page_data.append(result1)
    lock.acquire()
    cursor.execute("SELECT * FROM today_history order by `index` desc limit 5")
    lock.release()
    result2 = cursor.fetchall()
    first_page_data.append(result2)
    lock.acquire()
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit 5;")
    lock.release()
    result3 = cursor.fetchall()
    first_page_data.append(result3)
    return json.dumps(first_page_data)


@jftime.route("/hotAudios")
def hotAudios():
    first_page_data = []
    lock.acquire()
    cursor.execute("SELECT * FROM jfmt order by `index` desc limit 4")
    lock.release()
    result1 = cursor.fetchall()
    first_page_data = first_page_data+result1
    lock.acquire()
    cursor.execute("SELECT * FROM today_history order by `index` desc limit 3")
    lock.release()
    result2 = cursor.fetchall()
    first_page_data = first_page_data + result2
    lock.acquire()
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit 2")
    lock.release()
    result3 = cursor.fetchall()
    first_page_data = first_page_data + result3
    lock.acquire()
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit 4")
    lock.release()
    result4 = cursor.fetchall()
    first_page_data = first_page_data + result4
    print(first_page_data)
    return json.dumps(first_page_data)


@jftime.route("/dataLength")            # 获取节目数，进行分页
def dataLength():
    demo_dict = {}
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM jfmt")
    lock.release()
    result1 = cursor.fetchone()
    demo_dict["data1_len"] = result1['COUNT(*)']
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM today_history")
    lock.release()
    result2 = cursor.fetchone()
    demo_dict["data2_len"] = result2['COUNT(*)']
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM trump_twitter")
    lock.release()
    result3 = cursor.fetchone()
    demo_dict["data3_len"] = result3['COUNT(*)']
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM wenzhao")
    lock.release()
    result4 = cursor.fetchone()
    demo_dict["data4_len"] = result4['COUNT(*)']
    return json.dumps(demo_dict)


@jftime.route("/handleCurrentChange")              # 点击下一页、上一页
def handleCurrentChange():
    objects = request.args.get('objects')
    offset = int(request.args.get('offset'))
    if (objects == 'jfmt'):
        cursor.execute("SELECT * FROM jfmt order by `index` desc limit %s,5", offset)
        res = cursor.fetchall()
        return json.dumps(res)
    if (objects == 'today_history'):
        cursor.execute("SELECT * FROM today_history order by `index` desc limit %s,5", offset)
        res = cursor.fetchall()
        return json.dumps(res)
    if (objects == 'trump_twitter'):
        cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit %s,5", offset)
        res = cursor.fetchall()
        return json.dumps(res)