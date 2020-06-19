import random
from datetime import datetime
import sys


def main(num):
	user=0
	comp=0
	tied=0
	try:
		while num!=0:
			random.seed(9001)
			com=random.choice(['r','p','s'])

			random.seed(datetime.now())
			inpt=random.choice(['r','p','s'])
			if inpt == 'r' and com == 'p':
				comp+=1

			elif inpt=='p' and com=='s':
				comp+=1

			elif inpt=='s' and com=='r':
				comp+=1

			elif inpt == 'p' and com == 'r':
				user+=1

			elif inpt=='r' and com=='s':
				user+=1

			elif inpt=='s' and com=='p':
				user+=1
			else:
				tied+=1
			num-=1

	except KeyboardInterrupt:
		print('simulation interrupted by KeyboardInterrupt')
		print('simulations ran untill interrupted: {}'.format(num))
		exit

	print("Scores are ")
	print('user : {}'.format(user))
	print('comp : {}'.format(comp))
	print('tied : {}'.format(tied))
	print('')
	total=int(sys.argv[1])
	wins_user=user/total
	wins_comp=comp/total
	wins_tied=tied/total
	wins_user*=100
	wins_user= round(wins_user,2)
	wins_comp*=100
	wins_user=round(wins_comp,2)
	wins_tied*=100
	wins_tied=round(wins_tied,2)
	print('percentage A wins, B wins, tied: {}, {}, {}'.format(wins_user,wins_comp,wins_tied))

if __name__ == '__main__':
	main(int(sys.argv[1]))
	print('simulations ran : {}'.format(sys.argv[1]))

