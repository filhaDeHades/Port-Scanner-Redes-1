from socket import *

# Variáveis do servidor
serverName = "localhost"
serverPort = 80

# Variáveis do socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
setence = raw_input("Digite a mensagem:")

# Envio de dados
clientSocket.sendto(setence, (serverName,serverPort))

# Envio de dados
clientSocket.sendto(setence, (serverName,serverPort))

# Resposta
maxsizeMenssage = 1024 * 1 # tamanho em bytes
modifieldSetence, addr = clientSocket.recvfrom(maxsizeMenssage) # resposta,
print("From Server {}: {}".format(addr, modifieldSetence))

# Fechar sockets
clientSocket.close()