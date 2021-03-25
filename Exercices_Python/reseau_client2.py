#! /usr/bin/python3
import socket, sys

HOST, PORT = 'localhost', 12802

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    connect_activ = True
    while connect_activ:
        data = input('> ')
        sock.sendall(bytes(data + '\n', 'utf-8'))
        received = str(sock.recv(1024), 'utf-8')
        print(received)
        if data == 'fin':
            connect_activ = False

print('connexion closed')
