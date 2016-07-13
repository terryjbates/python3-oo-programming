#!/usr/bin/env python
from random import randint
from socket import *
from time import ctime

HOST = ''
PORT = 2437
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print("Waiting for connection on {}".format(PORT))
        tcpCliSock, addr = tcpSerSock.accept()
        print("...connected from: {}".format(addr))

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            data = str(data, 'utf-8')
            echo_data = "{} {}".format(ctime(), data)
            tcpCliSock.send(bytes(echo_data, "utf-8"))
        tcpCliSock.close()
except(KeyboardInterrupt, EOFError):
    tcpSerSock.close()
