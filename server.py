import socket, threading
from database import connect

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s:%s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s:%s" % (self.ip, self.port, ))
        self.clientsocket.recv(32).decode()

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

for i in range(2):
    tcpsock.listen()
    print( "En attente de nouvelle connexion...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
    
print("2 clients connectés")

while True:
    if(clientsocket.recv(32).decode() == "END"):
        break
    move = clientsocket.recv(32).decode()
    # print(move)
    
print("server stoped")