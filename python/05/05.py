#Ciclos "for" y listas

carros = ['Lamborghini', 'Ferrari', 'Porsche', 'Bugatti']

for x in carros:
    print(x)
    print(type(x))

print('\n\n')

print('Funcion *len*. len(carros): ', str(len(carros)))

for x in range(len(carros)):
    print(carros[x])
    print(type(x))

print('\n\n')

for x in range(3,101,15):
    print(x)
