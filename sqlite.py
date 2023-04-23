import sqlite3
import random
src='abcdefghijklmnopqrstuvwxyz'
def get_str(x, y):
    str_num=random.randint(x, y)
    astr=''
    for i in range(str_num):
        astr += random.choice(src)
    return astr
def output():
    cur.execute('select * from biao')
    for sid, name, ps in cur:
        print(sid, ' ', name, ' ', ps)
def output_all():
    cur.execute('select * from biao')
    for item in cur.fetchall():
        print(item)
def get_data_list(n):
    res=[]
    for i in range(n):
        res.append((get_str(2,4), get_str(8, 12)))
    return res
if __name__=='__main__':
    print("Connecting ...")
    con=sqlite3.connect(':memory:')
    print("Cursor...")
    cur=con.cursor()
    print("Create a table...,'biao'")
    cur.execute('create table biao(id integer  primary key autoincrement not null, name text, passwd taxt)')
    print('Insert a record...')
    cur.execute('insert into biao (name, passwd) values(?, ?)',(get_str(2, 4), get_str(8, 12),))
    print('Show all records...')
    output()
    print('Multiple records were inserted in batches')
    cur.executemany('insert into biao (name, passwd) values(?,?)', get_data_list(3))
    print('Show all recods...')
    output_all()
    print('Update a record...')
    cur.execute('update biao set name=? where id=?', ('aaa', 1))
    print('Show all records...')
    output()
    print('Delete a record...')
    cur.execute('delete from biao where id=?',(3,))
    print('Show all records: ')
    output()

