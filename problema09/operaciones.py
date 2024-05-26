#Utilizaremos una funcion validate para no tener redundancia en las funciones al realizar lo mismo
def validate(n1, n2) :
    try :
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        return 'Error: Tipo de dato no valido.'
    else :
        return n1, n2

def suma(n1, n2) :
    n1,n2 = validate(n1, n2)
    res = n1 + n2
    return res

def resta(n1, n2) :
    n1,n2 = validate(n1, n2)
    res = n1 - n2 
    return res

def multiplicacion(n1, n2) :
    n1,n2 = validate(n1, n2)
    res = n1 * n2 
    return res

#Utilizaremos un try except para detectar si el divisor es 0
def division(n1, n2) :
    n1,n2 = validate(n1, n2)
    try :
        res = n1 / n2
    except ZeroDivisionError :
        return 'No es posible dividir entre cero.'
    else :
        return res
