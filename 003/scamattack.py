'''
name: hgvjhb
email: fchgvjbh@hgvjhb.ve
city: 5
mobileNo: 1234567890
dob: 1992-02-20
panNumber: ANRPM2537J
employeeType: 1
annualSalary: 200000
'''

import requests
import os
import json
import string
import random
import rstr
import urllib.request
print(urllib.request.urlopen("https://www.timesmoney.in/lp/term-insurance/lead-process-new.php").getcode())


ch=string.ascii_letters+string.digits+'!@#$%^&*()'
random.seed=(os.urandom(1024))

url='https://www.timesmoney.in/lp/term-insurance/'
r=requests.get(url)
print(r.status_code)

email_services=['@yahoo.com','@gmail.com','@hotmail.com','@icloud.com','@mail.com','@msn.com','@outlook.com','@laposte.net']

names =json.loads(open('name.json').read())
cities=json.loads(open('city_num.json').read())


for name,city in zip(names,cities):
	name_extra=''.join(random.choice(string.digits))

	pan_format=rstr.xeger("[A-Z]{5}[0-9]{4}[A-Z]{1}")

	salary_format=rstr.xeger("[1-9][0]{5}")
	salary_format1=rstr.xeger("[5-9][0]{4}")
	salary_format2=rstr.xeger("[1-9][0]{4}")

	sal=[salary_format1,salary_format,salary_format2]
	salary=random.choice(sal)

	phone_format=rstr.xeger("[7-9][0-9]{9}")

	options=[1,2]
	opt=random.choice(options)

	dob=rstr.xeger("(19[6-9][0-9])-((0[1-9])|(1[0-2]))-(0[1-9]|(1[0-9]|2[0-8]))")
	num=rstr.xeger("([0-9]?|[0-9]|[0-9]{2}|[0-9]{3})")
	email_1=name.lower()+num+random.choice(email_services)
	full_name=name
	city_name=city
	pan=pan_format


	requests.post(url,allow_redirects=False,data={
		'name': full_name,
		'email': email_1,
		'city': city_name,
		'mobileNo': phone_format,
		'dob': dob,
		'panNumber': pan,
		'employeeType': opt,
		'annualSalary': salary
		})

	print(full_name,email_1,city_name,phone_format,dob,pan,opt,salary,sep='|')


