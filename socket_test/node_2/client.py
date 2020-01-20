# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
host = "127.0.0.1"
port = 1234
msg = ""
sock.connect((host, port))

while True:
    msg = input("Client: ")
    sock.send(msg.encode("utf-8"))
    msg = sock.recv(1024).decode("utf-8")
    print("Server: " + msg)

sock.close()