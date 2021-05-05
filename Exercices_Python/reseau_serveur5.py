#! /usr/bin/python3
# Définition d'un serveur réseau gérant un système de CHAT simplifié.
# Utilise les threads pour gérer les connexions clientes en parallèle.
import socket, sys, threading

HOST, PORT = 'localhost', 12820

class ThreadClient(threading.Thread):
    # dérivation d'un objet thread pour gérer la connexion avec client
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        # dialogue avec le client
        nom = self.getName()    # un nom par thread
        counter = 0
        while 1:
            msgClient = self.connexion.recv(1024).decode('Utf8')
            counter += 1
            if not msgClient or msgClient == 'fin':
                print(f'{self.getName()} sent {counter} messages')
                break
            message = f'{nom}> {msgClient}'
            print(message)
            # faire suivre à tous les clients sauf l'émetteur
            for cl in conn_client:
                if cl != nom:
                    conn_client[cl].send(message.encode('Utf8'))
                
        # fermeture de la connexion
        self.connexion.close()      # coupe connexion coté serveur
        del conn_client[nom]        # supprime client du dict
        print(f'client {nom} déconnecté')
        
# Initialisation du serveur - mise en place du socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind(((HOST, PORT)))
except socket.error:
    print("echec de la connexion du socket à l'adresse choisie")
    sys.exit()
else:
    print('serveur connecté et en attente de requêtes')
    mySocket.listen(5)
    
# prise en charge des requetes client
conn_client = {}        # dict des connexions client
while 1:
    connexion, addr = mySocket.accept()
    # creation d'un obj thread pr gerer la connexion
    th = ThreadClient(connexion)
    th.start()
    # connexion dans le dict client / th.getName() pr id du thread
    conn_client[th.getName()] = connexion
    print(f'client {th.getName()} connecté / IP: {addr[0]} / Port: {addr[1]}')
    # dialogue avec le client
    msg = 'Vous êtes connecté, envoyez vos messages.'
    connexion.send(msg.encode('Utf8'))
    