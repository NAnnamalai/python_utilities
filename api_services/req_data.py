import requests
import requests_cache
import json

requests_cache.install_cache('demo_cache')

r = requests.get('http://localhost:3000/employees')
employees = json.loads(r.text)

# display all employees
employee_attrs = employees[0].keys()
for employee in employees:
    print "-----------------------------------------"
    for key in employee_attrs:
        print "{} : {}".format(key, employee[key])
    print "-----------------------------------------"

# select a employee with id 361
print requests.get('http://localhost:3000/employees/361').json()

# select a employee with first_name Janet
print requests.get('http://localhost:3000/employees?first_name=Janet').json()

# delete a employee with id 839
print requests.delete('http://localhost:3000/employees/839')