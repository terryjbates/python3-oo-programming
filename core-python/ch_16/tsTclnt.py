#!/usr/bin/env python


import argparse
from socket import *

HOST = ''
PORT = 2437
BUFSIZ = 1024


def tcp_client(host, port):
    addr = (host, port)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(addr)
    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(bytes(data, "utf-8"))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            tcpCliSock.close()
            break
        print(str(data))
    tcpCliSock.close()


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
    tcp_client(host, port)
