import socket
import sys

TCP_IP = "127.0.0.1" #Define o ip de loopback como o ip do servidor
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
file_name = ''


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
    sock.connect((TCP_IP, FILE_PORT)) #Conecta-se ao servidor responsável por receber o nome do arquivo
    sock.send(file_name) #Envia o nome do arquivo
    sock.close() #Finaliza a comunicação

    print( "Sending %s ..." %file_name)

    f = open(file_name, "rb") #Abre o arquivo no módo binário para leitura
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
    sock.connect((TCP_IP, DATA_PORT)) #Conecta-se ao servidor responsável por receber as informações do arquivo
    data = f.read() #Lê os dados do arquivo
    sock.send(data) #Envia os arquivos

finally:
    sock.close() #Finaliza a conexão com o servidor
    f.close() #Fecha o arquivo