'''
Continuacion OOP: sobrecarga de operadores
'''


class vect(object):
    
    #Constructor de la clase
    #Todos los metodos (funciones) dentro de un 
    #objeto, llevan como parametro inicial "self"
    def __init__(self, data = []):
        self.data = data


    #Sobrecarga de suma, aplicado para un vector
    def __add__(self, sumando):
        x = []
        for i in range(len(self.data)):
            x.append(self.data[i] + sumando.data[i])
        return x

    #Sobrecarga de resta, aplicado para un vector
    def __sub__(self, substraendo):
        x = []
        for i in range(len(self.data)):
            x.append(self.data[i] - substraendo.data[i])
        return x        

    #Sobrecarga de string: devuelve la lista de datos del vector
    def __str__(self):
        return str(self.data)

    #Representacion cuando se invoca el objeto sin casting a STRING.
    def __repr__(self):
        return self.__str__()

    #Sobrecarga del operador de negacion
    def __neg__(self):
        x = []
        for i in self.data:
            x.append(-i)
        return x

    
