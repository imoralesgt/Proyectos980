#Tuplas

print('Libro: Python para todos')

print('------------------------')
print('********|Tuplas|********')
print('------------------------')
print('\n\nTupla \"diasDeLaSemana\":')
diasDeLaSemana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')
print(diasDeLaSemana)
print('Indice de \"Jueves\":',)
print(diasDeLaSemana.index('Jueves'))

print("Las tuplas son \"inmutables\" \n\n")

print("Tuplas, listas y diccionarios pueden\n\
contener elementos de distintos tipos\n")

print('Tupla \"remix\":')
remix = ('Texto', 4, 5.37, True)
print(remix)
for i in remix:
    print(type(i))

print("\n\n\nManejo de excepciones:\n")

try:
    #print(remix[6])
    print(remix['6'])
except IndexError as err:
    #pass
    print("El elemento no existe:", str(err))
except TypeError as err:
    print("El elemento es incorrecto:", str(err))



print('\n\nNo se pueden agregar o cambiar elementos de una tupla')
print('remix[0] = 10')
print('\nSe levanta una excepcion: TypeError')
remix[0]=10
