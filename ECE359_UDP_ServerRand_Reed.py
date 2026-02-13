# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:53:03 2026

@author: Jormungandr
"""

import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12000))

while True:
    rand=random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    if rand<4:
        continue
    serverSocket.sendto(message, address)