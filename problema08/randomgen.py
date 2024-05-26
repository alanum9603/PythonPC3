from random import *
#se genera una lista con valores del 1 al 100 y se ordena
def random_generator() :
    res = []
    for i in range(20) :
        res.append(randint(1,100))
    return res

def ordenar_lista(list) :
    list.sort()
    return list

def imprimir_lista(list) :
    print(list)