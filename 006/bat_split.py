import string
import re
import json

f=open(r"batman_q.txt","r", encoding="utf8")
#print(f.read())
lines=f.readlines()
print(len(lines[0]))
#print(lines[0][1:5])
character=[]
issue=[]
quote=[]
id=[]
n=0
for i in lines:
	name=i.split("–")
	quote.append(name[0])
	#print(name[-1])
	if re.search(r',', name[-1]):
		#print('yes')
		line=name[-1]
		line=line.split(',')
		character.append(line[0])
		issue.append(line[1])
		#print(name[-1])

	else:
		character.append(name[-1])
		issue.append('Not Found')
	n=n+1
	id.append(n)
data=[{'id':a, 'quote': n, 'quotee': i, 'issue':l} for a,n,i,l in zip(id,quote,character,issue)]

with open("batman_quotes.json","w") as f:
	json.dump(data,f,ensure_ascii=False,indent=4)
	print('json dump completed')