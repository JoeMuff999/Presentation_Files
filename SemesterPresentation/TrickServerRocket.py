#!/usr/bin/python
import sys
import socket

# Process the command line arguments.
#if ( len(sys.argv) == 2) :
#    trick_varserver_port = int(sys.argv[1])
#else :
#    print( "Usage: vsclient <port_number>")
#    sys.exit()

# Connect to the variable server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect( ("localhost", 53837) )

# Request the rocket position.
client_socket.send( "trick.var_pause()\n".encode() )
client_socket.send( "trick.var_ascii()\n".encode() )
client_socket.send( "trick.var_add(\"dyn.cannon.pos[0]\") \n".encode() +
                    "trick.var_add(\"dyn.cannon.pos[1]\") \n".encode()
                  )
client_socket.send( "trick.var_unpause()\n".encode() )

# Repeatedly read and process the responses from the variable server.
insock = client_socket.makefile("r")
while(True):
    line = insock.readline()
    if line == '':
        break

    print (line)
