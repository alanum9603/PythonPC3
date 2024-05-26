#Crearemos una lista con diccionarios para llamar más fácilmente a los datos
class Producto :
    producto = []
    def __init__(self, nombre : str, año : int) -> None:
        self.producto = [{'nombre':nombre, 'año': año}]

    def agregar(self, nombre : str, año : int) :
        producto = {'nombre':nombre, 'año':año}
        self.producto.append(producto)

    def mostrar(self) :
        return self.producto

#Creamos la clase catalogo, que herencia a la clase Producto y contiene la función para filtrar la lista    
class Catalogo(Producto) :
    res = []
    def __init__(self, producto) -> None:
        super().__init__(producto)
        pass
    
    #Utilizamos la lista para filtrar los datos por un for que verifique que el año coincide con la fecha para filtrar
    def filter_per_year(self, filter : int) :
        res = []
        for p in self.producto :
            if p['año'] == filter :
                res.append(p)
        return res

            


