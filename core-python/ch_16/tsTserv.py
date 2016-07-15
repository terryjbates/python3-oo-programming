#!/usr/bin/env python
from random import randint
from socket import *
from time import ctime
import argparse

HOST = ''
PORT = 2437
BUFSIZ = 1024


def tcpserver(host, port):
    addr = (host, port)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(addr)
    tcpSerSock.listen(5)

    try:
        while True:
            print("Waiting for connection on {}".format(port))
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
    except KeyboardInterrupt:
        tcpSerSock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="hostname to connect")
    parser.add_argument("--port", help="port to connect to")
    args = parser.parse_args()
    if args.port:
        port = args.port
    else:
        port = PORT
    if args.host:
        host = args.host
    else:
        host = HOST
    tcpserver(host, port)
