import pymysql
db = pymysql.connect("localhost","root","","TESTDB")
cursor=db.cursor()
sql="drop table if exists employee"
cursor.execute(sql)
sql="""create table employee(first_name char(2) not null,
    last_name char(20),
    age int,
    sex char(1),
    income float) """
cursor.execute(sql)
sql="""insert into employee(first_name, last_name, age, sex, incom) values ('Mac', 'Mohan', 20, 'M',2000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
sql="select * from employee where incom > '%d'"%(1000)
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print(fname, lname, age, sex, income)
except:
    print("Error: unable to fetch data")
db.close()

