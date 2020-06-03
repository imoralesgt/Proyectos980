#Listas

print('------------------------')
print('********|Listas|********')
print('------------------------')

print('\n\nLista \"nombres\"')
nombres = ['Juan','Pedro','Jose']
print(nombres)

print('\n\"append\". Agregar elemento al final: ')
nombres.append('Chepe')
nombres.append('Carlos')
print(nombres)

print('\n\"pop\". Extraer ultimo elemento de la lista y devolverlo:')
print(nombres.pop())
print(nombres)

print('\n\"pop\". Sobre algun otro elemento')
print(nombres.pop(1))
print(nombres)

print('\n\"del\". Eliminar elemento sin devolverlo')
del nombres[2]
print(nombres)

print('\n\"del\". Eliminar rango sin devolverlo')
del nombres[0:2]
print(nombres)

print('\n\"insert\". Insertar elementos a la lista en\n\
una posicion conocida')
nombres.insert(0,'Juan')
nombres.insert(1,'Pedro')
nombres.insert(2,'Jose')
print(nombres)


print('\n\"reverse\". Invertir elementos de posicion')
nombres.reverse()
print(nombres)

print('\n\nVamos a crear otra lista: \"animales\"')
animales = []

animales.append('Ardilla')
animales.append('Conejo')
animales.append('Quetzal')
animales.append('Cangrejo')
animales.append('Ballena')

print(animales)

print('\n\nPara acceder individualmente a un elemento de la lista')
print('\"animales[3]\"')
print(animales[3])

print('\nPara acceder a un rango de la lista')
print('\"animales[2:5]\"')
print(animales[2:5])

print('\nPara acceder a un rango de la lista')
print('\"animales[1:]\"')
print(animales[1:])

print('\nPara insertar multiples elementos a una lista')
animales.extend(['Tiburon', 'Cobra', 'Murcielago'])
print('animales.extend([\'Tiburon\', \'Cobra\', \'Murcielago\'])')
print(animales)



print('\n\nPara copiar listas, no solo hay que asignarlas')
print('Se copia por segmentacion\n')

print('a = [3,4,5,6,7]')
a = [3,4,5,6,7]

print('b = a')
b = a

print('print(str(b)) =>', str(b))

print('\n\ndel(a[2:4])')
del(a[2:4])
print('\nResulta, que se eliminaron elementos tambien en b')
print('Las listas a y b estan en la misma direccion de memoria:\n')
print('id(a), id(b)  =>  ', str(id(a)), ", ", str(id(b)))

print('Para copiar una lista (sin estar en la misma localidad de memoria):')
print('c = a[:]')
print('d = list(a)')
c = a[:]
d = list(a)

print('id(a), id(b), id(c), id(d)  =>  ', str(id(a)), ", ", str(id(b)), ", ", str(id(c)), ", ", str(id(d)))
