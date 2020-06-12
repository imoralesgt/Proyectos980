'''
Continuacion OOP: sobrecarga de operadores
'''

'''
Tarea 2:

Descripción detallada acá: https://bit.ly/3cUBEBm

Utilizando el mismo repositorio de tareas, ahora cree
una carpeta llamada T02, para agregar todo el código ahí.

Debe realizar una clase capaz de representar a una matriz 
de 1 o 2 dimensiones. Deberá analizar las características
del parámetro del constructor (vector, o matriz de 2 dimensiones) y
en función de eso, aplicar la sobrecarga de operadores para las
operaciones básicas de matrices:
    - Producto con un escalar
    - Suma/Resta de matrices
    - Multiplicación de matrices
    - Matriz inversa
    - Determinante
    

Asimismo, deberá crear (en el mismo archio de código fuente) las clases
necesarias para representar las excepciones relacionadas con operaciones inválidas.
Por ejemplo (pero no limitado a):
    - Al hacer el producto, si las dimensiones y tamaño son incorrectas
    - Al calular el determinante, si la matriz no es cuadrada
    - Al sumar/restar dos matrices, si las dimensiones y tamaño son incorrectas

NO es necesario crear excepciones de errores que ya existen: por ejemplo, si algún
dato es de tipo no numérico y se trata de hacer alguna operación aritmética. Este tipo
de Excepciones son, por ejemplo: ValueError, TypeError, etc.

'''


#Clase que representa un vector "optimizado" para realizar operaciones
#matemáticas directamente, reutilizando los operadores aritméticos
#nativos de Python 3, aplicado a operaciones de matrices de 1 dimensión.
class vect(object):
    
    #Constructor de la clase
    #Todos los metodos (funciones) dentro de un 
    #objeto, llevan como parametro inicial "self"
    def __init__(self, data = []):
        self.data = list(data)

    #La "longitud" del objeto, es en realidad representado
    #por la cantidad de datos de su lista principal
    def __len__(self):
        return len(self.data)

    def equalLenghts(self, nextObject):
        #Esto es posible, gracias a que se sobrecargó la
        #función __len__, de lo contrario, el código debería
        #haber sido así:
        #return len(self.data) == len(nextObject.data)
        return len(self) == len(nextObject) 


    #Sobrecarga de suma, aplicado para un vector
    def __add__(self, sumando):
        if self.equalLenghts(sumando):
            x = []
            for i in range(len(self.data)):
                x.append(self.data[i] + sumando.data[i])
            return vect(x)
        else:
            raise ErrorDimensional(len(self.data), len(sumando.data))

    #Sobrecarga de resta, aplicado para un vector
    def __sub__(self, sustraendo):
        if self.equalLenghts(sustraendo):
            x = []
            for i in range(len(self.data)):
                x.append(self.data[i] - sustraendo.data[i])
            return vect(x)        
        else:
            #Levantamos una excepcion creada a la medida
            raise ErrorDimensional(len(self.data), len(sustraendo.data))

    #Sobrecarga de multiplicacion, solo valida para producto con escalar
    #Debe hacerse en el siguiente orden: vector*escalar
    #de lo contrario, el objeto int y float deberian ser modificados
    def __mul__(self, escalar):
        if type(escalar) == int or type(escalar) == float:
            x = []
            for i in self.data:
                x.append(i*escalar)
            return vect(x)
        else:
            #La excepcion ya existe, solo se va a reutilizar
            raise TypeError("Solo pueden realizarse producto con un escalar")

    #Sobrecarga de string: devuelve la lista de datos del vector
    def __str__(self):
        return str(self.data)

    #Representacion cuando se invoca el objeto sin casting a STRING.
    def __repr__(self):
        return self.__str__()



    #Sobrecarga del operador de negacion
    def __neg__(self):
        if len(self):
            x = []
            for i in self.data:
                x.append(-i)
            return vect(x)
        else:
            raise VectorVacio

    
#Excepcion hecha a la medida, para reportar un error que no es estandar
#Se levanta esta excepcion cuando la longitud de dos vectores a sumar/restar
#no son iguales. Se reciben como parametros las longitudes de ambos vectores
class ErrorDimensional(Exception):
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    
    def __str__(self):
        return str("Las longitudes no coinciden: " + str(self.l1) + " ~= " + str(self.l2))

    def __repr__(self):
        return self.__str__()


#Excepción que se levanta cuando se trata de generar el inverso del vector,
#pero el vector está vacío
class VectorVacio(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return str("No hay elementos en la lista de datos")

    def __repr__(self):
        return self.__str__()


#Instancias de la clase de vector "mejorado" para ejemplo
a = vect([1,2,3,4,5])
b = vect([6,2,0,-3,8])
c = vect([3,8])
d = vect()



#Manejo de vector vacio
try:
    -d
except VectorVacio:
    vect()
