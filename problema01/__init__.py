from format import calculo_nivel_combustible

def main() :
    # Creamos una variable que va a mantener el bucle while ejecutandose hasta que se pueda recuperar los datos del nivel de combustible
    x = False

    while x == False :
        #Obtenemos una cadena de la que se van a obtener los valores para el calculo del nivel de combustible
        txt = input('Digite la fracción de combustible de su coche.\nDeben ser números enteros.\nUse el formato X/Y \n -> ')
        
        #Llamamos a la función que va a permitir obtener el nivel de combustible, asimismo, cambie el valor de x a True para finalizar el bucle
        x, nivel_combustible = calculo_nivel_combustible(txt)

    print(f'{nivel_combustible}')

if __name__ == '__main__' :
    main()