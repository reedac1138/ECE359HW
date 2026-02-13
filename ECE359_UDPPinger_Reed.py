# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:19:58 2026

@author: Jormungandr
"""

from socket import *
import time

serverName='localhost' 
serverPort=12000
clientSocket=socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
message = "ping"
x=0

while x<10:
    try:
        start = time.perf_counter()
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.perf_counter()
        r_tt = f"{(end-start)*1000: .2f}"
        print(modifiedMessage.decode(), x+1, r_tt, "ms")
    except timeout as e:
        print("Request", e)
        
    x=x+1
    

clientSocket.close()