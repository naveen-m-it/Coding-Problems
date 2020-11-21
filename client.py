"""this is created by Naveen M"""
#this is module header

import socket

#this is wanted variabls port and server ip

HEADER=64
PORT=5050
FORMAT="utf-8"
DISCONNECT_MESSAGE="!Disconneted"
SERVER="192.168.137.1"
ADDR=(SERVER,PORT)

#connect to a server and connect throuth the port number

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

#define a function for get message from server

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#send a message to the server

x=send(input(">>>"))
while x!= 'exit':
    x = input(">>>")
    send(x)
    continue

#if you enter exit the message will be disconneted

send(DISCONNECT_MESSAGE)