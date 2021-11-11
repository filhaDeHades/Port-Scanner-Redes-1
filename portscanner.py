import socket

def printResultados(resultados):
    for tipo in resultados:
        for porta in resultados[tipo]:
            print(f'{porta} : {tipo}')

def portScanner(lugar, inicio, final):
    resultados = {'disponivel': [], 'filtrada': [], 'fechada': []}
    for porta in range(inicio, final+1):
        dispCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dispCliente.settimeout(0.5)
        resp = dispCliente.connect_ex((lugar, porta))
        if (resp == 0):
            resultados['disponivel'].append(porta)
        elif (resp == 10035): # erro de time out
            resultados['filtrada'].append(porta)
        else:
            resultados['fechada'].append(porta)
    printResultados(resultados)

lugarUsuario = input("Digite o host a ser analisado: ")
rangeUsuario = list(map(int, input("Digite o range das portas a serem analisadas: ").split()))

portScanner(lugarUsuario, rangeUsuario[0], rangeUsuario[1])