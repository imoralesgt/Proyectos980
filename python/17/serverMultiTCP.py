#Referencia: https://realpython.com/python-sockets/

import socket
import selectors
import types


'''
Funciones "wrapper" utilizadas cada vez que se dispara un evento
Traten de entender estas funciones luego de haber leido el resto de
código que se ejecuta en el script principal
'''
def accept_wrapper(clientSocket):
    conn, addr = clientSocket.accept() #Se acepta la conexion remota
    print('Conexion aceptada de ', str(addr))

    conn.setblocking(False) #No queremos que sea una accion bloqueante

    #Aca se almacena la data de entrada y salida del socket
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')

    #Ahora que la conexión ha sido aceptada, estar preparados para
    #poder recibir o enviar informacion a través del socket
    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    #Se registra el nuevo tipo de "trigger" para lectura o escritura en socket
    sel.register(conn, events, data = data)


def service_connection(key, mask):
    clientSocket = key.fileobj
    data = key.data
    
    #Si el evento fue disparado porque ha llegado data al server
    if mask & selectors.EVENT_READ:
        recv_data = clientSocket.recv(BUFFER_SIZE)
        if recv_data:
            data.outb += recv_data #ponemos en el PIPE de salida del socket la data recibida
        else:
            print("Cerrando conexion con ", str(data.addr))
            sel.unregister(clientSocket) #Ya no es necesaria esta instancia de socket
            clientSocket.close()

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('Regresando ', repr(data.outb), ' a ', data.addr)
            sent = clientSocket.send(data.outb)

            #Se borran del buffer de salida los bytes que ya fueron enviados
            data.outb = data.outb[sent:]




'''
Codigo principal:
Acá se configuran los eventos a disparar las funciones wrapper
'''



SERVER_ADDR = ''
SERVER_PORT = 9800

BUFFER_SIZE = 1024

sel = selectors.DefaultSelector()

#TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Se levanta el servidor en la interfaz y puerto especificado
sock.bind((SERVER_ADDR, SERVER_PORT))
sock.listen()

print("Servidor escuchando en: ", str((SERVER_ADDR, SERVER_PORT)))


#Deja de ser una accion bloqueante
#Ahora se utilizaran handlers cuando llegue un request
#con la ayuda de selectores
sock.setblocking(False)

#Usando la característica multiparadigma de Python:
#Programación orientada a eventos!
sel.register(sock, selectors.EVENT_READ, data = None)


while True:
    #Bloqueamos la ejecucion, hasta que una solicitud de 
    #algun cliente llegue: ya sea para aceptar o transferir data
    events = sel.select(timeout = None)


    #Cada evento disparado por socket tiene una clave (identificador de socket)
    #y una máscara, que es un identificador único de cada evento disparado
    for key, mask in events:
        if key.data is None: #Si no viene nada de data, es solicitud para conectarse
            accept_wrapper(key.fileobj) #Entonces aceptamos la conexion
        else:
            service_connection(key, mask) #Si viene data, la recibimos

