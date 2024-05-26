import math
class Circulo :
    area = 0
    def __init__(self, radio : float) -> None:
        self.radio = radio
        pass

    def calc_area(self) :
        self.area += (self.radio ** 2) * math.pi
        return self.area
    
    def __str__(self) -> str:
        return f'Circulo de radio {self.radio}'
