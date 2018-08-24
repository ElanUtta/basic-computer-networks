import socket 
import sys

server = ''
port = 5558


tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
	tcpsoc.bind((server, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()


while 1:

    print('\nwaiting to receive message')
    data, address = tcpsoc.recvfrom(4096)
    data1, address1 = tcpsoc.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)
   

    if data == data1:
        print('envio 1')
        sent = tcpsoc.sendto('1'.encode('ascii'), address)
        print('sent {} bytes back to {}'.format(
            sent, address)) 
    else:
        print('envio 0')
        sent = tcpsoc.sendto('0'.encode('ascii'), address)
        print('sent {} bytes back to {}'.format(
            sent, address))



'''
    msg_recebida = cliente.recv(1024)
    msg = msg_recebida.decode('ascii')

    msg = "ark" + "\r\n"
    cliente.send(msg.encode('ascii'))
'''
