from faker import Faker
import json
import os
os.chdir("/home/paulcrickard/datalake")
fake=Faker()
for userid, _ in enumerate(range(1000), start=1):
    name=fake.name()
    fname=name.replace(" ","-")+'.json'
    data={
        "userid":userid,
        "name":name,
        "age":fake.random_int(min=18, max=101, step=1),
        "street":fake.street_address(),
        "city":fake.city(),
        "state":fake.state(),
        "zip":fake.zipcode()
    }
    datajson=json.dumps(data)


    with open(fname,'w') as output:
        output.write(datajson)
