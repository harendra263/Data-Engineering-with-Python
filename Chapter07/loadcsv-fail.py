from faker import Faker
import csv
with open('/home/paulcrickard/peoplepipeline/people.csv','w') as output:
    fake=Faker()
    header=['name','age','street','city','state','zip','lng','lat']
    mywriter=csv.writer(output)
    mywriter.writerow(header)
    for _ in range(1000):
        mywriter.writerow([fake.name(),fake.random_int(min=1, max=100, step=1), fake.street_address(), fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
print('{"status":"complete"}')
