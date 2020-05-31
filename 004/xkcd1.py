from time import sleep
import json
import random
import string
import json
import requests
import re
from bs4 import BeautifulSoup

url='https://xkcd.com/archive/'
import urllib.request
#print(urllib.request.urlopen(url).getcode())

page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
links=[]
labels=[]
data=soup.find('div', attrs={'id':'middleContainer'})
#label=data.text
#variable_final=[]


for data in soup.findAll('div', attrs={'id':'middleContainer'}):
	for a in data.findAll('a', href=True, text=True):
		links.append('https://xkcd.com' + a['href'])
		labels.append(a.text)

res = [{"label": n, "link": i} for n, i in zip(labels,links)]
print(type(res))


'''
for i in range(0,len(links)):
	print(type(labels[i]))
for entry in label.strip().split(","):
    variable_final = entry.lstrip()
    print(type(variable_final))
 '''   

with open("xkcd.json","w") as f:
	json.dump(res,f,indent=4)
	print('json dump completed')
