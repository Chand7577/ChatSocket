import socket

server_object=socket.socket()
port=8080


print("Socket has been created successfully!")
server_object.bind(('', port))

server_object.listen(2)
print("Socket is listening.... ")
conn,addr=server_object.accept()
print("Conncection establed from ",addr)
while True:
      data=conn.recv(1024).decode()
      if not data:
            break
      print("message ->",data)
      response=input("Would you like to send?")
      conn.send(response.encode()) 

conn.close()     
