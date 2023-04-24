import pymysql
db=pymysql.connect('localhost','root','','TESTDB')
cursor=db.cursor()
sql="insert into employee(first_name, last_name, age, sex, income) values ('Mac', 'Mohan', 20, 'M', 2000)"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
