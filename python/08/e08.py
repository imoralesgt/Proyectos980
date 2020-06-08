#Manejo de archivos de texto
#Explicar metodos de apertura de archivos: 'r','w','a','r+'

import time #Para generar pausa
import datetime #Para generar fecha/hora actual

def fileAppend(fileName = 'MiTexto.txt'):

    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'a') #Abrir para agregar a archivo existente
    archivo.write('\n\nNuevo evento de append...\n')
    print('Espere, agregando datos al archivo...')
    for i in range(20):
        hora = str(datetime.datetime.now().ctime())
        archivo.write(str(hora+' --> '+str(i)+'\n'))
        time.sleep(1)

    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('\n\nAppend finalizado')

def fileWrite(fileName = 'MiTexto.txt'):
    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'w') #Abrir para SOBREESCRIBIR el archivo existente
    archivo.write('Sobreescribiendo archivo...\n')
    print('Espere, sobreescribiendo el archivo...')
    for i in range(20):
        hora = str(datetime.datetime.now().ctime())
        archivo.write(str(hora+' --> '+str(i)+'\n'))
        time.sleep(1)

    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('Append finalizado')

def fileRead(fileName = 'MiTexto.txt'):
    archivo = open(fileName,'r') #Abrir el archivo en modo de LECTURA
    for line in archivo: #Leer cada linea del archivo
        print(line, end = '') #Imprimir linea por linea del archivo leido

    archivo.close() #Cerrar el archivo al finalizar