#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, "utf-8"), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(str(data))

udpCliSock.close()