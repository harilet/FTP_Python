from os import listdir, getcwd
from socket import *
from threading import *

global  client_list
client_list = list()


s=socket(AF_INET,SOCK_STREAM)
p=input("PORT:")
s.bind(('127.0.0.1',int(p)))
s.listen(50)

    
def recvfile(c):

    c.send("list".encode('utf-8'))
    for i in checkfiles.file_list:
        c.send(i.encode('utf-8'))
        c.send("::".encode('utf-8'))
    c.send("EOFlist".encode('utf-8'))

    while True:
        fil = c.recv(1024).decode('utf-8')
        print(fil)
        if fil == "stop":
            break
        try:
            fp = open(fil, "r")
            c.send("file".encode('utf-8'))
        except IOError:
            print("file ["+fil+"] NOT found")
            c.send(" 404".encode('utf-8'))
            continue

        for i in fp:
            c.send(i.encode('utf-8'))

        c.send(" stop ".encode('utf-8'))
        print("Send ["+fil+"] to "+str(c))
        fp.close()

def checkfiles():
    checkfiles.file_list = listdir(getcwd())
    while True:
        t_file_list=listdir(getcwd())
        if t_file_list!=checkfiles.file_list:
            print("Change in files")
            checkfiles.file_list=t_file_list

            for i in client_list:
                i.send("list".encode('utf-8'))
                i.send("::".encode('utf-8'))
                for j in checkfiles.file_list:
                    i.send(j.encode('utf-8'))
                    i.send("::".encode('utf-8'))
                i.send("EOFlist".encode('utf-8'))


t1 = Thread(target=checkfiles)
t1.start()

while (True):
    a, d = s.accept()
    client_list.append(a)
    t1 = Thread(target=recvfile, args=(a,))
    t1.start()

c.close()
s.close()
