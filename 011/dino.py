import numpy as np
from PIL import ImageGrab,Image
import pyautogui 
import cv2
import time
import click

#83 83 83
obstacle=r,g,b=83,83,83
def btn_clk(btn):
	pyautogui.keyDown(btn)
	print(btn)
	return


def kollide(fat):
	for i in range(476,506):
		for j in range(370, 391):
		      		if fat[i, j]==obstacle:#475 371 536 393
		      			btn_clk('up')
		      			return
'''
	for i in range(482,510):
		for j in range(349, 370):
			if fat[i, j] == obstacle:
				btn_clk('down')
				return
		'''

@click.command()
def main():

	print(r"""\
	                                                   ____
       ___                                      .-~. /_"-._
      `-._~-.                                  / /_ "~o\  :Y
          \  \                                / : \~x.  ` ')
           ]  Y                              /  |  Y< ~-.__j
          /   !                        _.--~T : l  l<  /.-~
         /   /                 ____.--~ .   ` l /~\ \<|Y
        /   /             .-~~"        /| .    ',-~\ \L|
       /   /             /     .^   \ Y~Y \.^>/l_   "--'
      /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
     Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
     |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
     |      ~---~           /   ~~"---\_  ' __[>
     l  .                _.^   ___     _>-y~
      \  \     .      .-~   .-~   ~>--"  /
       \  ~---"            /     ./  _.-'
        "-.,_____.,_  _.--~\     _.-~
                    ~~     (   _}       
                           `. ~(
                             )  \
                            /,`--'~\--'~\
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	""")
	print('AUTOMATED DINO-BOT')
	print('play this bot on		https://srijanreddy.github.io/target_rex.html')
	print('note: bot only works on this website')
	countdown()
	while True:
	      img = ImageGrab.grab()  
	      data = img.load()
	      kollide(data)

	      		
def countdown():
	
	timer=[5,4,3,2,1]
	for i in timer:
		print(i)
		time.sleep(1)




if __name__ == '__main__':
	main()
