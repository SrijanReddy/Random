import json
import requests
import lxml.html as lh
from bs4 import BeautifulSoup
import speech_recognition as sr
from gtts import gTTS 
import pygame

def play_sound(file_name):
	pygame.mixer.init()
	pygame.mixer.music.load(file_name)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)
	

def function(url1):	
	page=requests.get(url1)
	states=[]
	state_links=[]
	cases=[]
	deaths=[]
	recovered=[]
	soup=BeautifulSoup(page.content,'html.parser')
	data=soup.find('div', attrs={'id':'covid19-container'})
	for i in data.find_all('a', href=True, text=True):
		names=i.text
		if names=='UTC':
				break
		elif names[0].isalpha():
			states.append(names)
			state_links.append('https://en.wikipedia.org/'+i['href'])
	states=states[3:-13]
	state_links=state_links[3:-13]

	for row in data.findAll('tr'):
		cells=row.findAll('td')
		#print(len(cells))
		if len(cells)==4:
			cases.append(cells[0].find(text=True))
			deaths.append(cells[1].find(text=True))
			recovered.append(cells[2].find(text=True))
	        #E.append(cells[4].find(text=True))
	res = [{"state_name": n, "wiki_link": i,"cases": l, "deaths":u, "recovered": k} for n,i,l,u,k in zip(states,state_links,cases,deaths,recovered)]
	text='which state data do you wanna access?'
	speech = gTTS(text = text, lang = 'en', slow = False)
	speech.save('question.mp3')
	play_sound('question.mp3')
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("which state data do you wanna access?(speak now)")
		audio=r.listen(source)
	print(r.recognize_google(audio))
	finder=r.recognize_google(audio)

	for ii in res:
		if ii['state_name']==finder:
			text='The number of cases in '+ii['state_name']+' are '+ii['cases']+' and there have been '+ii['deaths']+' deaths and '+ii['recovered']+' recovered patients'
			speech = gTTS(text = text, lang = 'en', slow = False)
			speech.save('text.mp3')
			print(text)
			play_sound('text.mp3')
			#os.system('start text.mp3')

			print('thank you for use covid voice assistant')
