import math

class Circulo :
    area = 0
    def __init__(self, radio : float) -> None:
        self.radio = radio
        pass

    def calc_area(self) :
        self.area += round((self.radio ** 2) * math.pi, 2)
        return f'Circulo de radio {self.radio} y área {self.area}'
    
    def __str__(self) -> str:
        return f'Circulo de radio {self.radio}'

#En esta clase Cuadrilateto, se verificará el ancho y largo de la forma 
#para verificar si es un cuadrado o rectangulo
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
    

