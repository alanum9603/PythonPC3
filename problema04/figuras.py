#Utilizaremos un if en __str__() y calc_area() para validar si la medida de largo y ancho es igual, entonces será un cuadrado
#en caso contrario, será un rectangulo
class Cuadrilatero :
    area = 0
    def __init__(self, ancho : float, largo : float) -> None:
        self.ancho = ancho
        self.largo = largo
        pass

    def calc_area(self) :
        self.area += round(self.ancho * self.largo, 2)
        if self.ancho == self.largo :
            return f'Cuadrado de lado {self.ancho} y área {self.area}'
        else :
            return f'Rectangulo de base {self.ancho}, altura {self.largo} y área {self.area}'
    
    def __str__(self) -> str:
        if self.ancho == self.largo :
            return f'Cuadrado de lado {self.ancho}'
        else :
            return f'Rectangulo de base {self.ancho}, altura {self.largo}'