import json
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
from state import function
import speech_recognition as sr
from gtts import gTTS 
import os
import pygame

def play_sound(file_name):
	pygame.mixer.init()
	pygame.mixer.music.load(file_name)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)
	
text='Welcome to Covid-19 tracker, which country data do you wanna access?'
speech = gTTS(text = text, lang = 'en', slow = False)
speech.save('question.mp3')
play_sound('question.mp3')
sr.Microphone.list_microphone_names()
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
	r.adjust_for_ambient_noise(source)
	print("which country data do you wanna see?(speak now)")
	audio=r.listen(source)

print(r.recognize_google(audio))
finder=r.recognize_google(audio)

url='https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data'
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
data=soup.find('table', attrs={'id':'thetable'})

countries=[]
links=[]
num=[]
cases=[]
deaths=[]
recovered=[]
for i in data.find_all('a', href=True, text=True):
	names=i.text
	if names=='UTC':
			break
	elif names[0].isalpha():
		countries.append(names)
		links.append('https://en.wikipedia.org/'+i['href'])

countries=countries[4:]
links=links[4:]

for row in data.findAll('tr'):
    cells=row.findAll('td')
    #print(len(cells))
    if len(cells)==4:
        cases.append(cells[0].find(text=True))
        deaths.append(cells[1].find(text=True))
        recovered.append(cells[2].find(text=True))
        #E.append(cells[4].find(text=True))

res = [{"country_name": n, "wiki_link": i,"cases": l, "deaths":u, "recovered": k} for n,i,l,u,k in zip(countries,links,cases,deaths,recovered)]

#print(type(res))



for ii in res:
	if ii['country_name']==finder:
		#print('Country found')
		#print(ii['cases'])
		text='The number of cases in '+ii['country_name']+' are '+ii['cases']+' and there have been '+ii['deaths']+' deaths and '+ii['recovered']+' recovered patients'
		speech = gTTS(text = text, lang = 'en', slow = False)
		speech.save('text.mp3')
		print(text)
		play_sound('text.mp3')
		#os.system('start text.mp3')

		txt='do you want to search data in this country ?'
		speech = gTTS(text = txt, lang = 'en', slow = False)
		speech.save('txt.mp3')

		play_sound('txt.mp3')

		with mic as source:
			r.adjust_for_ambient_noise(source)
			print("do you want to search data in this country ?(yes/no)(speak now)")
			audio=r.listen(source)
		inpt=r.recognize_google(audio)
		
		if inpt=='yes' or inpt=='YES':
			new_url=ii['wiki_link']
			function(new_url)

