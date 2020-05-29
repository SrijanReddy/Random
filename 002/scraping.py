import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
from urllib.request import urlopen
import time
import os

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

#query=input("enter Movie name--")
def movie_timer(query):

	url=f'https://www.google.com/search?q='
	total_url=url+query+'%20movie%20duration'
	#print(total_url, end='\n')
	headers = {"user-agent" : USER_AGENT}

	try:
		resp = requests.get(total_url, headers=headers)
	except:
	    print("Error opening the URL",end='\n')
	if resp.status_code==200:
		print(resp.status_code)
		soup = BeautifulSoup(resp.text, 'lxml')
		data = soup.findAll('div', {'class': 'Z0LcW XcVN5d'})
		print(data[0].text,end='\n')
		time=data[0].text
		if(time[1]=='h'):
			hours=int(time[0])
			minutes=hours*60
			min1=int(time[3])
			min2=int(time[4])
			minut=(min1*10)+(min2)
			minutes=minutes+minut
			times=minutes*60
			try:
				os.system("shutdown /s /t {}".format(times))
			except Exception as e:
				print(e)
			return minutes
		else:
			minutes=int(time[0])
			times=minutes*60
			try:
				os.system("shutdown /s /t {}".format(times))
			except Exception as e:
				print(e)
			return minutes
	else:
		print('cant access the url')

	

