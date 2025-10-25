import socket 


PORT = 9199
HOST = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected with {address}")
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"Message from client {message}")
    communication_socket.send("Message received".encode("utf-8"))
    communication_socket.close()