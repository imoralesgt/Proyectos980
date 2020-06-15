import socket

IP_ADDRESS = '157.245.82.242'
IP_ADDRESS_ALL = ''
IP_PORT = 9800

#Si el buffer es menor al mensaje a enviar, la info llega incompleta
BUFFER_SIZE = 4096 #Debe ser menor al tamaño máximo del datagrama de IPv4 (64 KB)


# Se crea el socket UDP (SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Se levanta el servidor, y automáticamente comienza la escucha
# NO HAY CONEXIÓN DIRECTA CON NINGÚN CLIENTE
serverAddress = (IP_ADDRESS_ALL, IP_PORT)
print('Levantando servidor en {},  puerto {} \n\n'.format(*serverAddress))
try:

    sock.bind(serverAddress)

    while True:
        print('\nEsperando cualquier mensaje, de cualquier cliente...')
        data, address = sock.recvfrom(BUFFER_SIZE)

        print('\nRecibidos {} bytes desde {}'.format(len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print('Enviados de vuelta {} bytes a {}'.format(sent, address))

finally:
    print("Cerrando servidor...")
    sock.close()