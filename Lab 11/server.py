import socket
import sys
import threading
from datetime import datetime


class ClientThread(threading.Thread):
    def _init_(self, clientAddress, clientsocket):
        threading.Thread._init_(self)
        self.csocket = clientsocket

    def run(self):
        global cn
        self.csocket.send(bytes("Hi, I am the Server..",'utf-8'))
        print("Connection from : ", cn)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
              cn=cn-1
              break
            print("from client", msg)
            self.csocket.send(bytes(msg[::-1], 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")

cn=0
LOCALHOST = "127.0.0.1"
PORT = int(sys.argv[1])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    cn=cn+1
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()