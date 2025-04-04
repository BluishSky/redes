# cliente_udp.py
import socket

HOST = 'localhost'
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, servidor UDP!', (HOST, PORT))
    data, server = s.recvfrom(1024)

print('Resposta do servidor:', data.decode())
