#!/usr/bin/env python

from socket import *

HOST = ''
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)



while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, "utf-8"))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data).strip())
    tcpCliSock.close()
