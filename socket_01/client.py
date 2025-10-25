import socket

HOST =  socket.gethostbyname(socket.gethostname()) #IP of the server, not clients ip address
PORT = 9199

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))

socket.close()
