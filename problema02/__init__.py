from clases import list_to_int

def main() :
    notasaentero = []
    #Pediremos una cadena separando las notas por coma para después separarlos y crear la lista
    notas = input('Digite una lista de notas con valores separados por coma -> ')
    notasaentero = list_to_int(notas)
    print(notasaentero)

if __name__ == '__main__' :
    main()