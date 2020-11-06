import socket
host=socket.gethostname()
ip=socket.gethostbyname(host)
print(host)
print("your ip is",ip)
