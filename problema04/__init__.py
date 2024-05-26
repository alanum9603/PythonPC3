from figuras import Cuadrilatero as c

def main() :
    #Utilizamos un while y try except para poder asegurarnos de obtener un valor para el ancho y largo
    #y así poder crear el objeto rectangulo y calcular su área
    while True : 
        try :
            ancho = float(input('Digite el ancho del rectangulo -> '))
            largo = float(input('Digite el largo del rectangulo -> '))
        except : 
            print('Formato incorrecto. Solo pueden ser números enteros o decimales \nIntente nuevamente')
        else : 
            break
    rectangulo = c(ancho = ancho, largo = largo)
    area = rectangulo.calc_area()
    print(area)

if __name__ == '__main__' :
    main()