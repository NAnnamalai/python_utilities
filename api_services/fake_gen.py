# generating fake data using Faker package
# dumping them to json file
# using npm package json-server to serve api requests

# pip install Faker
# npm install -g json-server
# json-server --watch db.json
# pip install requests_cache

from faker import Faker
fake = Faker()
import json
import random

emp_id = []
first_name = []
last_name = []
company = []
job = []

no_of_employees = 10

for k in range(no_of_employees):
  emp_id.append(random.randint(1, 1000))
  first_name.append(fake.first_name())
  last_name.append(fake.last_name())
  company.append(fake.company())
  job.append(fake.job())

employee_data = {}
employee_data['employees'] = [{"id": o, "first_name": p, "last_name": q, "company": r, "designation": s} for o, p,q, r, s in zip(emp_id, first_name, last_name, company, job)]

# dictionary dumped as json in a json file
with open('db.json', 'w') as fp:
     json.dump(employee_data, fp, indent = 4)
