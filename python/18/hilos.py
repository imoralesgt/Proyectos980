'''
Ejemplo de programación concurrente con hilos
Hay algunas funciones comentadas, que son el 
equivalente, pero con procesamiento multinúcleo.
'''


import threading #Concurrencia con hilos
import time      #Retardos
import logging   #Logging
import sys       #Requerido para salir (sys.exit())

#Para fines demostrativos
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
    format = '[%(levelname)s] (%(threadName)-10s) %(message)s'
    )

# logging.basicConfig(
#     level = logging.DEBUG, 
#     format = '[%(levelname)s] (%(processName)-10s) %(message)s'
#     )


#Lanza el primer hilo con los parámetros:
#name: Nombre "humano" para identificar fácil al hilo
#target: La función a ejecutar (o método de un objeto)
#args: argumentos, deben ser enviados como tupla
#daemon: servicio corriendo de fondo -> permite detener el hilo con "Thread._stop()"
t1 = threading.Thread(name = 'Contador de 1 segundo',
                        target = contador,
                        args = (range(100), ),
                        daemon = True
                        )

t2 = threading.Thread(name = 'Contador rapido',
                        target = contador,
                        args = ((range(250), 0.2)),
                        daemon = True
                        )

listaHilos = []

for i in range(20):
    listaHilos.append(
        threading.Thread(name = 'Contador ' + str(i),
                        target = contador,
                        args = (()),
                        daemon = True
                        )
    )





# p1 = multiprocessing.Process(name = 'Contador de 1 segundo',
#                         target = contador,
#                         args = (range(25), )
#                         )

# p2 = multiprocessing.Process(name = 'Contador rapido',
#                         target = contador,
#                         args = ((range(200), 0.2))
#                         )

#Luego de configurar cada hilo, se inicializan

t1.start()
t2.start()

for i in listaHilos:
    i.start()

# p1.start()
# p2.start()

#Programa principal

cnt = 0

try:
    while True:
       logInfo2 = 'Contador: ' + str(cnt)
       logging.info(logInfo2) 


       cnt += 1

       time.sleep(5)


except KeyboardInterrupt:
    
    logging.INFO("Terminando hilos")
    
    if t1.isAlive():
        t1._stop()
    
    if t2.isAlive():
        t1._stop()


    # if p1.is_alive():
    #     p1.terminate()
    
    # if p2.is_alive():
    #     p2.terminate()

finally:
    sys.exit()
