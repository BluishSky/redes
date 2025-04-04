# servidor_tcp.py
import socket

HOST = 'localhost'
PORT = 12345

# Cria o socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor TCP escutando em {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Recebido:", data.decode())
            conn.sendall(b"Mensagem recebida!")
