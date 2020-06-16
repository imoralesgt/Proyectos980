#socket.sendfile() disponible desde Python 3.3

import socket

SERVER_ADDR = ''
SERVER_PORT = 9800


BUFFER_SIZE = 8 * 1024 #8 KB para buffer de transferencia de archivos

server_socket = socket.socket()
server_socket.bind((SERVER_ADDR, SERVER_PORT))
server_socket.listen(100) #1 conexion activa y 9 en cola
try:
    while True:
        print("\nEsperando conexion remota...\n")
        conn, addr = server_socket.accept()
        print('Conexion establecida desde ', addr)
        print('Enviando archivo de prueba de 5MB...')
        with open('file5M', 'rb') as f: #Se abre el archivo a enviar en BINARIO
            conn.sendfile(f, 0)
            f.close()
        conn.close()
        print("\n\nArchivo enviado a: ", addr)
finally:
    print("Cerrando el servidor...")
    server_socket.close()