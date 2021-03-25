
import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print(f'le serveur ecoute à présent sur le port {port}')

connexion_avec_client, infos_connexion = connexion_principale.accept()
print('infos connexions:', infos_connexion)


msg_recu = b''
while msg_recu != b'fin':
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message reçu comporte des accents
    print(msg_recu.decode())
    # confirmation de reception avec '5/5'
    connexion_avec_client.send(b'5/5')

print('fermeture de la connexion')
connexion_avec_client.close()
connexion_principale.close()

