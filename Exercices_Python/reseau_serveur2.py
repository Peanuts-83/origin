#! /usr/bin/python3
import socket, select, readchar

hote = ''
port = 12801

# Exit by pressing 'q'
"""
def key_out():
    if readchar.readkey() == 'q':
        print(serveur_lance)
        serveur_lance = False
"""

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print(f"le serveur ecoute à présent sur le port {port}")

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # attente de connexion client(rlist) / ecoute connexion_principale / attente 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 1)
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        print('nouveau client connecté:', infos_connexion)
        clients_connectes.append(connexion_avec_client)

    # ecoute des clients connectés (renvoyés par select) / try pour gerer exception si vide
    client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
    except select.error:
        print('select.error')
        pass
    except BrokenPipeError:
        print('BrokenPipeError')
    else:
        for client in client_a_lire:
            msg_recu = client.recv(1024)
            msg_recu = msg_recu.decode()
            print(f'Reçu: {msg_recu}')
            client.send(b'5/5')
            # client retiré de la liste des connectés / client fermé
            # le serveur reste en ligne!
            if msg_recu == 'fin':
                print(f'Client {client.getpeername()} is leaving')
                clients_connectes.remove(client)
                client.close()
        # check for exit
        #key_out()
            

print('fermeture de la connexion')
for client in clients_connectes:
    client.close()
connexion_principale.close()





