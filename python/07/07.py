#Ciclos while

"""
---------
|Tarea 1|
---------

Entrega martes 09/06/2020 antes de la hora de la clase (11:00 hrs GMT-6)

***************************************************

Problema 1
----------
Encontrar los primeros N numeros perfectos
Como sugerencia, puede implementar una funcion que encuentre
los divisores propios de un numero, y devuelva una lista con estos
N es un numero que ingresa el usuario
http://es.wikipedia.org/wiki/N%C3%BAmero_perfecto


Problema 2
----------
Encontrar los primeros N numeros amigos.
Debe preguntar al usuario el valor de N antes de iniciar.
http://es.wikipedia.org/wiki/N%C3%BAmeros_amigos


***************************************************
"""

def numOfDigits(num): #Calcular la cantidad de digitos de un entero
    cnt = 0
    while(num): #Mientras que el numero sea distinto de 0
        cnt += 1
        num = num // 10
    return cnt

def splitDigits(num):
    res = [] #Lista donde se almacena resultado
    divisor = 10**numOfDigits(num) // 10 #Cantidad de 0 a agregar al final
    while(num):
        x = num // divisor
        res.append(x)
        num %= divisor
        divisor //= 10
    return res

numeros = (555, 777, 46235, 32135, 2123513215321, 321532) #Un conjunto aleatorio

print('Numeros originales')
for i in numeros:
    print(str(i))

print('\nDigitos separados')

for i in numeros:
    print(str(splitDigits(i)))