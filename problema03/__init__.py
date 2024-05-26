from figuras import Circulo as c

def main() :
    #Utilizamos un while y try except para poder asegurarnos de obtener un valor para r
    #y así poder crear el objeto círculo y calcular su área
    while True :
        try : 
            r = float(input('Digite el radio del circulo -> '))
        except :
            print('Formato invalido, intentelo nuevamente')
        else : 
            break
    circulo = c(radio = r)
    area = circulo.calc_area()
    print(area)

if __name__ == '__main__' :
    main()