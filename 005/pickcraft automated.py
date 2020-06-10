from ppadb.client import Client
import numpy
import time
from PIL import Image

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()


device = devices[0]
#print(device)
num=0
while(num!=100):
	device.shell('input swipe 500 500 500 500')
	num=num+1
	if num==20:
		print(num)