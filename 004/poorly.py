from time import sleep
import json
import random
import string
import json
import requests
import re
from bs4 import BeautifulSoup

url='http://www.poorlydrawnlines.com/archive/'
import urllib.request
#print(urllib.request.urlopen(url).getcode())

page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
links=[]
labels=[]
data=soup.find('div', attrs={'class':'content page'})
#label=data.text

for a in data.findAll('a', href=True, text=True):
	links.append(a['href'])
	labels.append(a.text)

res = [{"label": n, "link": i} for n, i in zip(labels,links)]
print(res)





 

with open("poorlydrawnlines.json","w") as f:
	json.dump(res,f,ensure_ascii=False,indent=4)
	print('json dump completed')
