#Separacion de digitos usando funciones integradas de Pyton 3

def splitDigits2(num): #Convertimos a string y 
    num = str(num)
    x = []
    for i in num:
        x.append(int(i))
    return x


numeros = (555, 777, 46235, 32135, 2123513215321, 321532) #Un conjunto aleatorio

for i in numeros:
    print(str(splitDigits2(i)))
    