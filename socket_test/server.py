# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
host = socket.gethostname()
port = 1234
sock.bind(("", port))

sock.listen(4)
print("Host: %s waiting for connections..." %(host))

while True:
    client, address = sock.accept()
    print(address," connected.")
    message = "Thank you, client."
    client.send(message.encode("utf-8"))
    client.close()