#!/usr/bin/python
from pynput.keyboard import Key, Controller

import sys
import socket
import time

keyboard = Controller()

x = 0
savex=0
savey=0
y = 0
t = 0
counterx = 0
countery = 0


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect( ("localhost", 63548) )

client_socket.send( "trick.var_pause()\n".encode() )
client_socket.send( "trick.var_ascii()\n".encode() )
client_socket.send( "trick.var_add(\"dyn.cannon.pos[0]\") \n".encode() +
                    "trick.var_add(\"dyn.cannon.pos[1]\") \n".encode() +
                    "trick.var_add(\"dyn.cannon.time\") \n".encode()
                  )
client_socket.send( "trick.var_unpause()\n".encode() )

insock = client_socket.makefile("r")
time.sleep(10)

while(True):
    line = insock.readline()
    if line == '':
        break
    t,x,y,z =  line.split()
    x = float(x)
    y = float(y)
    counterx = x-savex/1
    countery = y-savey/1
    if countery > 0:
        while countery > 0:
            keyboard.press('w')
            time.sleep(.01)
            keyboard.release('w')
            time.sleep(.01)
            countery = countery-1
    else:
        countery = countery*-1
        while countery > 0:
            keyboard.press('s')
            time.sleep(.01)
            keyboard.release('s')
            time.sleep(.01)
            countery = countery-1
    
    while counterx > 0:
        keyboard.press('d')
        time.sleep(.01)
        keyboard.release('d')
        time.sleep(.01)
        counterx = counterx-1
    
    
        
        
    savex =x
    savey =y
    
    print (line)
