import pymysql
db = pymysql.connect('localhost', 'root', '', 'TESTDB')
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print('Database version: %s '%data)
db.close()
