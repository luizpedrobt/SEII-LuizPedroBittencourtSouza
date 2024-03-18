import socket
import time
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizará o datagram, uma forma que prevê canais de comunicação bidirecionais para envio de pacotes de dados. Não há garantia na entrega dos pacotes e podem haver inversões de ordem. Além disso, será utilizado os protocolos associados ao IPv4
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #O socket começa o envio do nome do arquivo
print("Sending %s ..." % file_name)

f = open(file_name, "r") #O arquivo é aberto em modo de leitura
data = f.read(buf) #Os dados lidos são armazenados. Os dados são armazenados em chunks de 1024bytes
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #O socket começa o envio dos dados
        data = f.read(buf) #Um novo chunk de dados é armazenado para o envio na próxima iteração
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() #Finaliza a comunicação
f.close() #Fecha o arquivo
