import socket
import sys
import threading
import time

#criando um socket object
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ("Failed to creat socket")
	sys.exit()

print("Socket conectado")

host = ""
port = 5558

s.connect((host, port))

print("Conexao e bind criada...")
print("Esta conectado a: localhost on port" , port)

def envia(s):

	msg = input("Diz: ")
	s.send(msg.encode('ascii'))
	s.send(msg.encode('ascii'))
	


def recebe(s):

	msg_recebida = s.recv(1024)
	msg_rec = msg_recebida.decode('ascii')
	
	if(msg_rec == '1'):
		print("Mensagem enviada com sucesso!!")
	if msg_rec == '0':
		print("Envio falho, enviar novamente!!")
		envia(s)

	return 1


def tempo():

	time.sleep(6)
	return 1



dado = False

while 1:
	print(len(threading.enumerate()) , "Numero de threads em execução")
	envia(s)
	t = threading.Thread(target=tempo)
	t.start()
	#inicia a thread em recebe, para que possamos verificar se o tempo já acabou
	t_rec = threading.Thread(target=recebe, args=(s,))
	t_rec.start()

	while not dado:
		if not t_rec.isAlive():
			dado = 1 #então a mensagem foi enviada com sucesso, e já podemos mandar mais
		if not t.isAlive():
			dado = 1#então o tempo acabou e deve-se mandar a mensagem de novo



s.shutdown(socket.SHUT_RDWR)
s.close()
#200.17.77.89