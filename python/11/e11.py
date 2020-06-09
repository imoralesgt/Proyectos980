def esPar(num):
    if(num%2 > 0):
        return False
    else:
        return True


for i in range(100):

    if(esPar(i)):
        print(i, "es par")
