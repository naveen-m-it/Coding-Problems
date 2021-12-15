"""this is created by Naveen M"""
#wanted modules for tcp connection
import socket
import threading

#variables for using store ip port nuners
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE="!Disconneted"

#create server and combine port and host 

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

#connect server to client and send a message to the client

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                 connected = False

#reply to the client
            print(f"[{addr}] {msg}")
            conn.send(input(">>>").encode(FORMAT))
        
    conn.close()
#running server command...
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
print("[SERVER] Server is starting...")
start()#this is using to start the server don't forget to call the funtion to start the server
