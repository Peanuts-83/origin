#! /usr/bin/python3
# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).
import socket, sys, threading

HOST, PORT = 'localhost', 12820

class ThreadReception(threading.Thread):
    # objet thread gérant la réception des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        while 1:
            msg = self.connexion.recv(1024).decode('Utf8')
            print(msg)
            if not msg or msg == 'fin':
                break
            # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        th_E.stop = True
        print('client arrêté - connexion interrompue')
        self.connexion.close()
        exit()
            
class ThreadEmission(threading.Thread):
    # objet thread gérant l'émission des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        while 1:
            msg = input()
            self.connexion.send(msg.encode('Utf8'))
            
# programme principal - etablissement de la connexion
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((HOST, PORT))
except socket.error:
    print('la connexion a échoué')
    sys.exit()
else:
    print('connexion établie avec le serveur')

            
# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
#th_E.daemon = True
#th_R.daemon = True
th_E.start()
th_R.start()