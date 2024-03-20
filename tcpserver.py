import socket
import threading

bind_ip="192.168.1.6"
bind_port=31036  


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server.bind((bind_ip,bind_port))

server.listen(5)

print("listening on port and ip ",bind_port ,bind_ip)



def handle_client(client_socket):
	request=client_socket.recv(1024)

	print("Data send by client ",request.decode())

	client_socket.send("Hello Host!".encode())
       	
	client_socket.close()


while True:
	client,addr=server.accept()
	print("Accepted connection from ",addr[0],addr[1])
	client_handler=threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
		
