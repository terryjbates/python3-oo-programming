#!/usr/bin/env python
from random import randint
from socket import *
from time import ctime

HOST = ''
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print("Waiting for message on {}".format(PORT))
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        data = str(data, 'utf-8')
        echo_data = "{} {}".format(ctime(), data)
        udpSerSock.sendto(bytes(echo_data, "utf-8"), addr)
        print("... received from and returned to {}".format(addr))
except(KeyboardInterrupt, EOFError):
    udpSerSock.close()
