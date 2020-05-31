import random
import json
from time import sleep
import string
import requests
import re
from bs4 import BeautifulSoup

def generate_poor():
 	data =json.loads(open('poorlydrawnlines.json').read())
 	rand=random.choice(data)
 	label=rand['label']
 	link=rand['link']
 	page=requests.get(link)
 	soup=BeautifulSoup(page.content,'html.parser')
 	images = soup.findAll('img')[1]
 	img=images.get("src")
 	return label,img


