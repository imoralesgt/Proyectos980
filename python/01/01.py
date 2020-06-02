#Introduccion a sintaxis de Python 3

#Este es un comentario de una linea

'''
Este es un comentario
de varias lineas
'''


#Si uno lo desea, se pueden imprimir los comentarios
#de multiples lineas

print(
'''
=======================
Analogia con lenguaje C
=======================
#include <stdio.h>

int a = 10;

if(a < 5){
    printf("a es menor a 5");
}else{
    printf("a es mayor o igual a 5");
}
'''
)

#Codigo equivalente en Python
#Al ser lenguaje interpretado,
#no requiere declaracion de variables

#No se usan llaves, sino indentaciones (tabulaciones)

print("\n\n\n")

a = 10

if a < 5:
    print("a es menor a 5")
else:
    print("a es mayor o igual a 5")


#Para leer entradas del teclado, se usa input()
b = input("Ingrese el valor de b: ")
if b.isdigit(): #Funcion especial .isdigit() de objetos tipo "string"
    b = int(b) #Type casting (conversion de tipos)
    print("b es entero ahora")

print("el tipo de b es ", str(type(b)), "   concatenacion \n\n") #Type devuelve el tipo de variable/objeto

print(type("texto"))
print(type(1234))
print(type(1234.0))
print(type(True))
print(type(0x20))
print(type((4,5)))
print(type([]))
print(type({}))
