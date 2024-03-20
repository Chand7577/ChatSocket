import socket


targetPort=93
targetHost="0.0.0.0"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((targetHost,targetPort))

request="Hello!,Mr.Robot"
client.send(request.encode())


response=client.recv(4096)

print(response)
