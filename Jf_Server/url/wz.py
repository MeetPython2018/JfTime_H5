from flask import Blueprint,make_response,send_from_directory,request,jsonify,Flask
from data import cursor,db
import json
import threading

lock = threading.Lock()


wz = Blueprint('wz', __name__)
app = Flask(__name__)


@wz.route("/dataAudio")
def dataAudio():
    lock.acquire()
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit 10;")
    result = cursor.fetchall()
    lock.release()
    return json.dumps(result)


@wz.route("/dataLength")            #获取节目数，进行分页
def dataLength():
    demo_dict = {}
    lock.acquire()
    cursor.execute("SELECT COUNT(*) FROM wenzhao")
    result = cursor.fetchone()
    demo_dict["data_len"] = result['COUNT(*)']
    lock.release()
    return json.dumps(demo_dict)


@wz.route("/handleCurrentChange")
def handleCurrentChange():
    offset = int(request.args.get('offset'))
    cursor.execute("SELECT * FROM wenzhao order by `index` desc limit %s,10", offset)
    result = cursor.fetchall()
    return json.dumps(result)

