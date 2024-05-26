import operaciones as op

def main() :
    n1 = input('Digite el 1er número -> ')
    n2 = input('Digite el 2do número -> ')
    print(f"""
Suma            ->  {op.suma(n1, n2)}
Resta           ->  {op.resta(n1, n2)}
Multiplicación  ->  {op.multiplicacion(n1, n2)}
División        ->  {op.division(n1, n2)}
""") 

if __name__ == '__main__' :
    main()