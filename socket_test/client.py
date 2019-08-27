# -*- coding: utf-8 -*-

import socket
import getpass

sock = socket.socket()
host = "127.0.0.1"
port = 1234
msg = ""
sock.connect((host, port))

while True:
    username = input("Enter username: ")
    password = getpass.getpass(prompt = "Enter password: ")
    sock.send(username.encode("utf-8"))
    sock.send(password.encode("utf-8"))
    break

sock.close()