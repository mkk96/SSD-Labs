import socket
import sys

SERVER = "127.0.0.1"
PORT = int(sys.argv[1])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
in_data =  client.recv(1024)
print("From Server :" ,in_data.decode())
while True:
  a = input("Enter the string you want to send:")
  client.sendall(bytes(a, 'UTF-8'))
  if a == 'bye':
    break
  in_data = client.recv(1024)
  print("From Server :", in_data.decode())
client.close()