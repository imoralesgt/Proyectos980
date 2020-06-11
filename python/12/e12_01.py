
#Funcion  -> Metodo
#Variable -> Atributo

#Clase fecha
class Fecha(object):
    
    #Metodo Constructor
    def __init__(self, dia, mes, anio):
        
        #Crear variables globales dentro de la clase
        #con la informacion que era local dentro 
        #del metodo constructor
        self.day = dia
        self.month = mes
        self.year = anio

    #Devolver una fecha como una tupla
    def mostrarFecha(self):
        x = (self.day, self.month, self.year)
        return x

    #Modificar la fecha almacenada dentro del objeto
    def cambiarFecha(self, dia, mes, anio):
        self.day = dia
        self.month = mes
        self.year = anio

    #Sobrecarga de operador a conversion a string (str)
    def __str__(self):
        return str((str(self.day) + "/" + str(self.month) + "/" + str(self.year)))


    #Sobrecarga de operador de representacion: devuelve string mandatoriamente
    def __repr__(self):
        return str(self.mostrarFecha())





miCumple = Fecha(7,12,1989)
revolucion = Fecha(20,10,1944)
independencia = Fecha(15,9,1821)