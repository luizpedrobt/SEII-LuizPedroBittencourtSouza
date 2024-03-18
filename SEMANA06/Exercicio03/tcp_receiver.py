import socket

TCP_IP = "127.0.0.1" #Define o ip de loopback como o ip do servidor
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
sock_f.bind((TCP_IP, FILE_PORT)) #O socket criado é associado a um servidor e uma porta
sock_f.listen(1) #O socket criado é colocado em modo de escuta. Ele pode lidar com uma conexão por vez

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Cria um objeto socket(descritor de arquivo) que será responsável pela comunicação do servidor. Este socket utilizara a forma de comunicação stream que provê canais de comunicação bidirecional ponto-a-ponto. Além disso, será utilizado os protocolos associados ao IPv4
sock_d.bind((TCP_IP, DATA_PORT)) #O socket criado é associado a um servidor e uma porta 
sock_d.listen(1) #O socket criado é colocado em modo de escuta. Ele pode lidar com uma conexão por vez


while True:
    conn, addr = sock_f.accept() #Espera uma conexão. Quando esta for recebida, um novo socket será criado e será responsável pela comunicação da mesma. Além disso é retornada a porta que o cliente está utilizando
    data = conn.recv(buf) #Recebe os dados enviados pelo sender no socket_f
    if data: #Se dados forem recebidos, 
        print("File name:", data)
        file_name = data.strip() #Remove os espaços no inicio e no fim dos dados recebidos

    f = open(file_name, 'wb') #Abre o arquivo no modo binário para escrita

    conn, addr = sock_d.accept() #Recebe os dados enviados pelo sender no socket_d

    while True:
        data = conn.recv(buf) #Recebe os dados enviados pelo sender no socket_d
        if not data: #Se nenhum dado for recebido a escrita termina
            break
        f.write(data) #Escreve os dados no arquivo

    print("%s Finish!" %file_name)
    f.close() #Fecha o arquivo
