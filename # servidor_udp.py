# servidor_udp.py
import socket

HOST = 'localhost'
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor UDP escutando em {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        print("Recebido de", addr, ":", data.decode())
        s.sendto(b"Mensagem recebida via UDP!", addr)

