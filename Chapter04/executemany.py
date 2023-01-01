import psycopg2 as db
from faker import Faker
fake=Faker()
data = [
    (i, fake.name(), fake.street_address(), fake.city(), fake.zipcode())
    for i, _ in enumerate(range(1000), start=2)
]
data_for_db=tuple(data)
print(data_for_db)
conn_string="dbname='dataengineering' host='localhost' user='postgres' password='postgres'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
print(cur.mogrify(query,data_for_db[1]))
cur.executemany(query,data_for_db)
conn.commit()
query2 = "select * from users"

cur.execute(query2)
print(cur.fetchall())


