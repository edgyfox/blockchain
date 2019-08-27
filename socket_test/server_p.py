# -*- coding: utf-8 -*-

import socket
import threading
import _thread

#print_lock = threading.Lock()

def threaded(client, address):
    
    while True:
        data = client.recv(1024).decode("utf-8")
        username = data
        data = client.recv(1024).decode("utf-8")
        password = data
        print(username, password)
        if data == "!":
            print("Ending connection with", address)
#            print_lock.release()
            data = "Bye" + str(address)
            break
        else:
            print("Client " + str(address) + " for server: " + data)
            data = input("Server for client " + str(address) + ": ")
        client.send(data.encode("utf-8"))
    client.close()
    
host = ""
port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
print("Listening to port", port)

while True:
    
    print("Waiting for connection...")
    client, address = sock.accept()
#    print_lock.acquire()
    print("Connected to", address)
    _thread.start_new_thread(threaded, (client, address))
    
sock.close()