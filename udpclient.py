import socket

target_port=80
target_host="www.google.com"

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"A",(target_host,target_port))
data,addr=client.recv(4096)

print(data)
