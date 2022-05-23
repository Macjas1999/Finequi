from concurrent.futures import thread
import socket
import threading
import datetime
from tkinter import mainloop

# inner imports
from Actor import Actor
from Client import Client
from Listener import Listener

print("[MAIN MENU]\n"+
"1. Listening\n"+
"2. Client")
userMenuInput = input("Choose a number: ")
mainLoop = True

while mainLoop:
    if userMenuInput == "1":
        listenerTest = Listener(socket.gethostbyname(socket.gethostname()), 5555, "Disconnected")
        listenerTest.listenStart()
    elif userMenuInput  == "2":
        testClient1 = Client(socket.gethostbyname(socket.gethostname()), 5555, "Disconnected")
        
        newA = Actor("Test", "Test", datetime.datetime.now(), "Test", 2137, "Test")
        testClient1.send(newA.dataBundle())
        testClient1.send(testClient1.DISSCN_MESSAGE)
        userMenuInput = input("send again: ")
        if userMenuInput == "2":
            continue
        else:
            mainLoop = False