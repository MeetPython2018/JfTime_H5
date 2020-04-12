from flask import Blueprint,make_response,send_from_directory,request,jsonify,Flask,session
from data import cursor,db
import json
import threading

lock = threading.Lock()


jftime = Blueprint('jftime', __name__)
app = Flask(__name__)

@jftime.route("/jfmt")
def jfmt():
    lock.acquire()
    cursor.execute("SELECT * FROM jfmt order by `index` desc limit 5")
    result = cursor.fetchall()
    lock.release()
    return json.dumps(result)


@jftime.route("/today_history")
def today_history():
    lock.acquire()
    cursor.execute("SELECT * FROM today_history order by `index` desc limit 5")
    result = cursor.fetchall()
    lock.release()
    return json.dumps(result)


@jftime.route("/trump_twitter")
def trump_twitter():
    lock.acquire()
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit 5")
    result = cursor.fetchall()
    lock.release()
    return json.dumps(result)


@jftime.route("/hotAudios")
def hotAudios():
    first_page_data = []
    lock.acquire()
    cursor.execute("SELECT * FROM jfmt order by `index` desc limit 4")
    result1 = cursor.fetchall()
    first_page_data = first_page_data+result1
    cursor.execute("SELECT * FROM today_history order by `index` desc limit 3")
    result2 = cursor.fetchall()
    first_page_data = first_page_data + result2
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit 2")
    result3 = cursor.fetchall()
    first_page_data = first_page_data + result3
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit 4")
    result4 = cursor.fetchall()
    lock.release()
    first_page_data = first_page_data + result4
    return json.dumps(first_page_data)


@jftime.route("/PullAudios")
def PullAudios():
    first_page_data = []
    lock.acquire()
    cursor.execute("SELECT * FROM jfmt order by `index` desc limit 5")
    result1 = cursor.fetchall()
    first_page_data.append(result1)
    cursor.execute("SELECT * FROM today_history order by `index` desc limit 5")
    result2 = cursor.fetchall()
    first_page_data.append(result2)
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit 5;")
    result3 = cursor.fetchall()
    first_page_data.append(result3)
    lock.release()
    return json.dumps(first_page_data)


@jftime.route("/dataLength")            #获取节目数，进行分页
def dataLength():
    demo_dict = {}
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM jfmt")
    result1 = cursor.fetchone()
    demo_dict["data1_len"] = result1['COUNT(*)']
    cursor.execute("SELECT COUNT(*) FROM today_history")
    result2 = cursor.fetchone()
    demo_dict["data2_len"] = result2['COUNT(*)']
    cursor.execute("SELECT COUNT(*) FROM trump_twitter")
    result3 = cursor.fetchone()
    demo_dict["data3_len"] = result3['COUNT(*)']
    cursor.execute("SELECT COUNT(*) FROM wenzhao")
    result4 = cursor.fetchone()
    demo_dict["data4_len"] = result4['COUNT(*)']
    lock.release()
    return json.dumps(demo_dict)


@jftime.route("/handleCurrentChange")
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


@jftime.route("/handleCurrentChange1")
def handleCurrentChange1():
    offset = int(request.args.get('offset'))
    cursor.execute("SELECT * FROM jfmt order by `index` desc limit %s,5", offset)
    res = cursor.fetchall()
    return json.dumps(res)


@jftime.route("/handleCurrentChange2")
def handleCurrentChange2():
    offset = int(request.args.get('offset'))
    cursor.execute("SELECT * FROM today_history order by `index` desc limit %s,5", offset)
    res = cursor.fetchall()
    return json.dumps(res)


@jftime.route("/handleCurrentChange3")
def handleCurrentChange3():
    offset = int(request.args.get('offset'))
    cursor.execute("SELECT * FROM trump_twitter order by `index` desc limit %s,5", offset)
    res = cursor.fetchall()
    return json.dumps(res)