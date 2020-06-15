import socket

# Crea un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ADDR = '157.245.82.242' #La IP donde desea levantarse el server
IP_ADDR_ALL = '' #En caso que se quiera escuchar en todas las interfaces de red
IP_PORT = 9800 #Puerto al que deben conectarse los clientes

BUFFER_SIZE = 16 * 1024 #Bloques de 16 KB

# Bind the socket to the port
serverAddress = (IP_ADDR_ALL, IP_PORT) #Escucha en todas las interfaces
print('Iniciando servidor en {}, puerto {}'.format(*serverAddress))
sock.bind(serverAddress) #Levanta servidor con parametros especificados

#Existe una nueva funcion en Python 3.8: socket.create_server()
#Tiene poca documentación aún, por lo que utilizaremos socket.bind() + socket.listen()

# Habilita la escucha del servidor en las interfaces configuradas
sock.listen(10) #El argumento indica la cantidad de conexiones en cola

while True:
    # Esperando conexion
    print('Esperando conexion remota')
    connection, clientAddress = sock.accept()
    try:
        print('Conexion establecida desde', clientAddress)

        # Se envia informacion en bloques de BUFFER_SIZE bytes
        # y se espera respuesta de vuelta
        while True:
            data = connection.recv(BUFFER_SIZE)
            print('Recibido: {!r}'.format(data))
            if data: #Si se reciben datos (o sea, no ha finalizado la transmision del cliente)
                print('Enviando data de vuelta al cliente')
                connection.sendall(data)
            else:
                print('Transmision finalizada desde el cliente ', clientAddress)
                break
    
    except KeyboardInterrupt:
        sock.close()

    finally:
        # Se baja el servidor para dejar libre el puerto para otras aplicaciones o instancias de la aplicacion
        connection.close()