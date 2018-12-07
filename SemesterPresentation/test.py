from pynput.keyboard import Key, Controller

import sys
import socket
import time

counter = 0
keyboard = Controller()
time.sleep(5)

keyboard.press('d')
time.sleep(.01)
keyboard.release('d')
time.sleep(.01)
keyboard.press('d')
time.sleep(.01)
keyboard.release('d')
keyboard.press('d')
keyboard.release('d')
keyboard.press('d')
#while counter < 100:
	#keyboard.press('d')
	##time.sleep(.1)
	#keyboard.release('d')
	#counter+=1
