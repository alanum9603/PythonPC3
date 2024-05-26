import randomgen as rg

def main() :
    res = []
    res = rg.random_generator()
    print('Lista con números del 1 al 100')
    rg.imprimir_lista(res)
    print('Lista ordenada')
    rg.ordenar_lista(res)
    rg.imprimir_lista(res)
    
main()