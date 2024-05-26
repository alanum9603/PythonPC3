from clases import Producto, Catalogo

def main() :
    #Utilizamos dos while, el primero para crear el objeto,
    #el segundo se utiliza para crear el menú
    while True :
        try :
            nombre = input('Digite el nombre del producto -> ')
            año = int(input('Digite el año de producción -> '))
        except :
            print('Error. Digite los valores correctamente (nombre=cadena, año=entero)')
            continue
        else : 
            productos = Producto(nombre=nombre, año=año)
            print(productos.mostrar())
            break
    #Este bucle contiene todo el menu, contiene también otro bucle while en su interior para llamarlo cuando 
    #ya se haya seleccionado una opción del menú y evitar regresar almenú en caso se digite mal
    while True :
        try :
            x = int(input('¿Qué desea hacer?\n1. Mostrar productos\n2. Agregar otro producto\n3. Filtrar productos\n4. Salir\n -> '))
        except :
            print('Error, digite un valor perteneciente al menú')
        else :
            match(x) :
                case 1 :
                    print(productos.mostrar())
                case 2 :
                    while True :
                        try :
                            nombre = input('Digite el nombre del producto -> ')
                            año = int(input('Digite el año de producción -> '))
                        except :
                            print('Error, Digite los valores correctamente (nombre=cadena, año=entero)')
                            continue
                        else : 
                            productos.agregar(nombre=nombre, año=año)
                            print(productos.mostrar())
                            break
                case 3 : 
                    filter = int(input('Digite año para filtrar -> '))
                    c = Catalogo.filter_per_year(productos, filter=filter)
                    print(c)
                case 4 :
                    break
                case _ :
                    print('Error, digite un número perteneciente al menú')
                    continue

if __name__ == '__main__' :
    main()