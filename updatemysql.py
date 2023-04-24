import pymysql
db=pymysql.connect("localhost","root","","TESTDB")
cursor=db.cursor()
sql="updata employee set age=age+1 where sex='%c'"%('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
