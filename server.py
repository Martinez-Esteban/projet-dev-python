import socket

socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ecoute.bind(('', 15556))
socket_ecoute.listen()

connexion_client, adresse_client = socket_ecoute.accept()

connexion_client.sendall(b'Hey my name is Olivier!')
socket_ecoute.close()