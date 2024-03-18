import socket
import select

UDP_IP = "127.0.0.1" #Define o ip de loopback como o ip do servidor
IN_PORT = 5005
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizará o datagram, uma forma que prevê canais de comunicação bidirecionais para envio de pacotes de dados. Não há garantia na entrega dos pacotes e podem haver inversões de ordem. Além disso, será utilizado os protocolos associados ao IPv4
sock.bind((UDP_IP, IN_PORT)) #O socket criado é associado a um servidor e uma porta

while True:
    data, addr = sock.recvfrom(1024) #Recebe chunks de dados do servidor e seu endereço
    if data: #Se dados forem recebidos
        print("File name:", data)
        file_name = data.strip() #Remove os espaços no inicio e no fim dos dados recebidos

    f = open(file_name, 'wb') #Abre o arquivo no modo binário para escrita

    while True:
        ready = select.select([sock], [], [], timeout) #Espera até o scoket estiver pronto para receber dados. Caso não receba dados em até 3 segundos, a operação é abortada
        if ready[0]: #Se o socket receber algum dado
            data, addr = sock.recvfrom(1024) #A variavel data recebe um chunk de 1024 bytes
            f.write(data) #Escreve os dados recebidos no arquivo
        else: #Se ele não receber 
            print("%s Finish!" % file_name)
            f.close() #O arquivo é fechado e a comunicação interrompida 
            break