import figuras as f
def main() :
    n1 = 0
    n2 = 0
    #En este bucle while se utiliza un match case para verificar de que forma se desea obtener el área, 
    #de esta forma, solicitar los datos según la forma que se especifica
    while True :
        try :
            x = int(input("¿Qué operación desea realizar?\n1. Circulo\n2. Rectángulo\n3. Cuadrado\n -> "))
            match x :
                case 1 : 
                    n1 = float(input('Digite la medida del radio del círculo -> '))
                    figura = f.Circulo(radio=n1)
                case 2 : 
                    n1 = float(input('Digite la medida del ancho del rectangulo -> '))
                    n2 = float(input('Digite la medida del largo del rectangulo -> '))
                    figura = f.Cuadrilatero(ancho=n1,largo=n2)
                case 3 : 
                    n1 = float(input('Digite la medida del lado del cuadrado -> '))
                    figura = f.Cuadrilatero(ancho=n1,largo=n1)
                case _ :
                    continue
            print(figura.calc_area())
        except ValueError :
            print('Error: Tipo de dato no valido.')
        else : 
            break

if __name__ == '__main__' :
    main()