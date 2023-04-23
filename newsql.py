import pymysql
db=pymysql.connect('localhost', 'root', '', 'TESTDB')
cursor=db.cursor()
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
sql="""create table employee(
        first_name char(2) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)"""
cursor.execute(sql)
db.close()

