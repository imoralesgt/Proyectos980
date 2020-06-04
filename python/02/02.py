#Operadores en Python

print(
"""
OPERADORES ARITMETICOS
SUMA: +
RESTA: -
PRODUCTO: *
COCIENTE: /
FLOOR DIVISION: //
MODULO:   %
POTENCIA: **
OPERADORES LOGICOS
NOT: ~     Alt+126
NOT: not
AND: and
OR:  or
COMPARACION
IGUAL: ==
DISTINTO: !=
MENOR QUE: <
MENOR O IGUAL QUE: <=
MAYOR QUE: >
MAYOR O IGUAL QUE: >=
"""
)

#Calculadora Basica en Python
#Referirse a "holaMundo3.c" para codigo en C

print("Bienvenid@ a la calculadora basica en Python\n\n")

bandera = True

n1 = input("Ingrese n1: ") #Leer texto que el usuario ingresa
if n1.isdigit():
    n1 = int(n1)
else:
    bandera = False

n2 = input("Ingrese n2: ") #Hay que convertir los numeros a int
if n2.isdigit():
    n2 = int(n2)
else:
    bandera = False

if bandera == True:

    print("La suma es:", str(n1+n2))
    print("La resta es:", str(n1-n2))
    print("El producto es:", str(n1*n2))

    if(n2!=0):
        print("El cociente es:",str(n1/n2))
        print("Division entera (floor) es:", str(n1//n2))
    else:
        print("Division sobre 0")

    print("La potencia es:",str(n1**n2))

    if(n2!=0):
        print("El residuo es:",str(n1%n2))
    else:
        print("Division sobre 0")

else:
    print("Ambas entradas deben ser numeros enteros")