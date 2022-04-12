import socket

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect(('localhost', 15556))

response = connexion_serveur.recv(1024)
print(response.decode())

connexion_serveur.close()