'''
Ejemplo de programación concurrente con multiprocesos
'''

import time      #Retardos
import logging   #Logging
import sys       #Requerido para salir (sys.exit())
import multiprocessing #Procesamiento multinucleo

#Esta función será lanzada en múltiples hilos, con distintos parámetros
def contador(rango = range(100), delay = 1):
    for i in rango:
        
        #Para hacer depuracion, ya no usaremos print()
        logText = "Contador: " + str(i)
        logging.debug(logText)

        time.sleep(delay) #Delay en segundos



#Configuracion inicial para logging. logging.DEBUG muestra todo.
logging.basicConfig(
    level = logging.DEBUG, 
    format = '[%(levelname)s] (%(processName)-10s) %(message)s'
    )

#Lanza el primer proceso con los parámetros:
#name: Nombre "humano" para identificar fácil al proceso
#target: La función a ejecutar (o método de un objeto)
#args: argumentos, deben ser enviados como tupla

p1 = multiprocessing.Process(name = 'Contador de 1 segundo',
                        target = contador,
                        args = (range(25), )
                        )

p2 = multiprocessing.Process(name = 'Contador rapido',
                        target = contador,
                        args = ((range(200), 0.2))
                        )

#Luego de configurar cada proceso, se inicializan
p1.start()
p2.start()



#Programa principal
cnt = 0

try:
    while True:
       logInfo2 = 'Contador: ' + str(cnt)
       logging.info(logInfo2) 


       cnt += 1

       time.sleep(5)


except KeyboardInterrupt:
       
    if p1.is_alive():
        p1.terminate()
    
    if p2.is_alive():
        p2.terminate()

finally:
    sys.exit()
