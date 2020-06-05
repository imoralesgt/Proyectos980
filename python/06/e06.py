#Funciones

#No es necesario declarar el tipo de dato que se retorna
#La misma funcion puede devolver cualquier tipo de dato

#Los parametros que se reciben pueden ser de cualquier tipo

#Esto aumenta la flexibilidad, pero hace mas dificil la depuracion,
#ya que hay que verificar que los parametros recibidos y devueltos
#sean validados antes o despues de ejecutar la funcion: para evitar una excepcion

def suma(n1, n2):
    x = n1 + n2
    return x

#Funcion con parametro por defecto
def sumaPorDefecto(n1, n2 = 0):
    x = n1 + n2
    return x
    
#Funcion con parametros por defecto
def sumaPorDefecto2(n1, n2, n3, n4 = 1, n5 = 1):
    x = n1 + n2 + n3 + n4 + n5
    return x

#Suma de un vector que se recibe como argumento
def sumaVector(arr = []):
    x = 0
    for i in arr:
        x += i
    return x

'''
Ejecutar desde un script externo, invocando:
"import e06"
"from e06 import *
"import e06 as operaciones"
'''