import pymysql
db = pymysql.connect(host="localhost",
                     user="root",
                     password="154303",
                     db="jfandwz",
                     cursorclass=pymysql.cursors.DictCursor,
                     charset="utf8")
cursor = db.cursor()