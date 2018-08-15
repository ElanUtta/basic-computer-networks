import socket
import sys

#criando um socket object
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ("Failed to creat socket")
	sys.exit()

print("Socket conectado")

host = ""
port = 5558

s.connect((host, port))

print("Conexao e bind criada...")

print("Esta conectado a: localhost on port" , port)
while True:
	msg = s.recv(1024)
	print(msg.decode('ascii'))

	arquivo = input("Escreva aqui o arquivo que deseja:")

	#manda a requisição 
	msg = 'GET / HTTP/1.1\n/' + arquivo 
	s.sendall(msg.encode('ascii'))

	msg = s.recv(1024)
	print(msg.decode('ascii'))

	s.shutdown(socket.SHUT_RDWR)
	s.close()
	break
#200.17.77.89