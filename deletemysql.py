import pymysql
db=pymysql.connect("localhost","root","","TESTDB")
curcor=db.cursor()
sql="delete from employee where age > '%d'"%(20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
