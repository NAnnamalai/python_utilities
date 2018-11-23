import requests
import requests_cache
import json
import logging

base_url = 'http://localhost:3000/employees'

logging.basicConfig(filename='warnings.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

requests_cache.install_cache('demo_cache')

r = requests.get(base_url)
employees = json.loads(r.text)

# display all employees
employee_attrs = employees[0].keys()
for employee in employees:
    print "-----------------------------------------"
    for key in employee_attrs:
        print "{} : {}".format(key, employee[key])
    print "-----------------------------------------"

# select a employee with id 361
print requests.get(base_url + '/361').json()

# select a employee with first_name Janet
print requests.get(base_url + '/?first_name=Janet').json()

# test a employee id 93 which is not present
if ~(len(requests.get(base_url + '/?id=93').json())):
    logging.warning('id %s not present in db', 93)

# test a employee name Marcia which is not present
if ~(len(requests.get(base_url + '/?first_name=Marcia').json())):
    logging.warning('name %s not present in db', "Marcia")

# delete a employee with id 839
if requests.delete(base_url + '/employees/839').status_code == 404:
    logging.warning('id %s not present in db', 839)