def list_formatter(lista : str) :
    res=[]
    #Eliminamos los espacios para evitar errores al convertir los valores a int
    lista.replace(' ','')
    #Agregamos los valores separando los valores por coma, pero se guardarán como cadena, en lugar de entero
    res = lista.split(',')
    return res

def list_to_int(list : str) :
    res = []
    listformat = list_formatter(list)
    #Listamos los valores de nota de la lista para verificar si se pueden convertir a int 
    #y en caso afirmativo se agregaran a la nueva lista, en caso contrario,
    #se imprimirá que este valor no se pudo convertir
    for l in listformat :
        try :
            res.append(int(l))
        except : 
            print(f'El valor {l} no se pudo convertir porque no es un entero')
            pass
    return res
