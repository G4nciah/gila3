import socket

hn = socket.gethostname()
ip = socket.gethostbyname(hn)

print("nombre de la pc:" + hn)
print("ip:" + ip)