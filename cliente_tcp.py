# cliente_tcp.py
import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, servidor TCP!')
    data = s.recv(1024)

print('Resposta do servidor:', data.decode())
