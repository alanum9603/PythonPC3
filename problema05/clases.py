class Alumno :
    notas = []
    def __init__(self, nombre : str, numeroRegistro : int) -> None:
        self.nombre = nombre
        self.numeroRegistro = numeroRegistro
        pass
    
    #Se devuelven los datos agregados
    def Display(self) :
        res = f'Nombre: {self.nombre} \nNúmero de registro: {self.numeroRegistro}'
        return res

    #Agregaremos un dato extra, la edad
    def setAge(self, edad : int) :
        self.edad = edad
        pass

    #Le aplicamos una función que separe los valores por coma
    #y agregamos la lista a nuestro objeto
    def setNota(self, nota : str) :
        listnota = notas_formatter(nota)
        for n in listnota :
            self.notas.append(n)
        pass

    def detailDisplay(self) :
        res = f'Nombre: {self.nombre} \nNúmero de registro: {self.numeroRegistro}\nEdad: {self.edad}\nNotas: {self.notas}'
        return res

#Reutilizamos una función de un ejercicio anterior para separar las notas por coma
def notas_formatter(lista : str) :
    res=[]
    strsinesp = lista.replace(' ','')
    res = strsinesp.split(',')
    for n, l in enumerate(res) :
        try :
            res[n] = int(l)
        except : 
            print(f'El valor {l} no se pudo agregar a la lista')
    return res
    