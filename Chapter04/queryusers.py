import psycopg2 as db
conn_string="dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "select * from users"
cur.execute(query)
print(cur.fetchone())
print(cur.rowcount)
print(cur.rownumber)
print(cur.fetchmany(3))
print(cur.rownumber)
with open('fromdb.csv','w') as f:
    conn=db.connect(conn_string)
    cur=conn.cursor()
    cur.copy_to(f,'users',sep=',')
f=open('fromdb.csv','r')
print(f.read())


