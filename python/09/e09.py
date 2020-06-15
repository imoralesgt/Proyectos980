LISTADO = 'listado.csv'

datos = []

archivo = open(LISTADO, 'r')
for linea in archivo:
    registro = linea.split(',')
    
    #registro[-1] = registro[-1].split(' \n')[0]
    registro[-1] = registro[-1].replace(' \n', '')  


    datos.append(registro)

archivo.close()

for i in datos:
    print(i)
    