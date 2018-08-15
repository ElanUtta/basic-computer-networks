import socket 
import sys

server = ''
port = 5558


tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	tcpsoc.bind((server, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

tcpsoc.listen(5) 
print( 'Socket now listening')

while 1:
    #wait to accept a connection - blocking call
    cliente, end_cliente = tcpsoc.accept()
    print ('Connected with ' + end_cliente[0] + ':' + str(end_cliente[1]))

    msg = "Qual arquivo deseja ?" + "\r\n"
    cliente.send(msg.encode('ascii'))

    msg_recebida = cliente.recv(1024)
    msg = msg_recebida.decode('ascii')


	#trata os dados recebidos do cliente
    msg_new = msg.split('/')
    print(msg_new[-1])
    nome_arquivo = msg_new[-1]

    arquivo = False
    try:
    	arquivo = open(nome_arquivo, 'r+b')
    	

    except:
		#ocorre o erro
        print("Arquivo não encontrado no servidor")
        msg = "ERROR 404 PAGE NOT FOUD\n"
        cliente.send(msg.encode('ascii'))
        
    

	#O arquivo é enviado
    if arquivo:
    	cliente.sendfile(arquivo)
    	cliente.close()

#bind to googles ip tcpsoc.send('HTTP REQUEST') response = tcpsoc.recv()