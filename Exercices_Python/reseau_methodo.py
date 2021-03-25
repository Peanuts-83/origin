### premier terminal / Serveur
import socket
# constructeur socket avec 2 params pr connection TCP
connexion_princ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connection du socket, ouverture du port 12800 (entre 1024 et 65535) et ecoute avec 'bind'
connexion_princ.bind(('', 12800))
# défini nbre de connexions max sur port 12800
connexion_princ.listen(5)
# accepter connexion client / bloque le progr en attente d'une connexion client
connexion_client, infos_connexion = connexion_princ.accept()


### second terminal / Client
import socket
# constructeur socket avec 2 params pr connection TCP
connexion_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# créer connexion client/serveur / sur même machine, nom d'hote est 'localhost'
connexion_serv.connect(('localhost', 12800))
# connexion activée, terminal 1 est débloqué et renvoie infos à 'print(infos_connexion)'

### 1er terminal
# terminal débloqué, vérification client
print(infos_connexions)
# ('127.0.0.1', 64803) >> IP localhost, port client
# methodes send/recv
connexion_client.send(b'connexion acceptee')
# 18 >> nbr de caract de la chaine de bytes


### 2eme terminal
# 1024 bytes par defaut, si + gd, reste recupéré après
msg_recu = connexion_serv.recv(1024)
msg_recu
# b'connexion acceptee'


### fermeture connexion
# des 2 cotés, nom_connexion.close()
connexion_princ.close()
connexion_client.close()
