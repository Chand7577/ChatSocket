import socket

client=socket.socket()
client.connect(('127.0.0.1',8080))
chat_=input("Enter a message or exit to leave ...")
while chat_.strip()!='exit':
    client.send(chat_.encode())
    data=client.recv(1024).decode()
    print("message ->",data)
    chat_=input("Enter a message or exit to leave")

client.close()
