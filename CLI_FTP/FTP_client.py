import socket
from threading import *
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter.filedialog import askopenfilename

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

def download():

    while TRUE:
        mess = s.recv(5).decode('utf-8')
        if mess in 'list':
            li=""
            while 'EOFlist' not in mess:
                mess = s.recv(1024).decode('utf-8')
                li=li+mess
            value=li.split("::")
            value.remove("list")
            value.remove("EOFlist")
            print(value)
            print(":")
        elif mess in "file":
            while " stop " not in mess:
                mess=s.recv(1024).decode('utf-8')
                print(mess)
        elif mess in " 404":
            print("File not found")


def req_file():
    while TRUE:
        mess=input(":")
        print(mess)
        s.send(mess.encode('utf-8'))


t1=Thread(target=req_file)
t1.start()

t2=Thread(target=download)
t2.start()
