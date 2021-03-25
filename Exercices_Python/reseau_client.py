
import socket

hote = 'localhost'
port = 12801

connexion_avec_serveur= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print(f'connexion etablie avec le serveur sur le port {port}')

msg_a_envoyer = b''
while msg_a_envoyer != b'fin':
    msg_a_envoyer = input('> ')
    # Pas de carract spéciaux ni d'accents
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())

print('fermeture de la connexion')
connexion_avec_serveur.close()

