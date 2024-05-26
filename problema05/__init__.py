from clases import Alumno as a 

def main() :
    #Se utilizaron 3 whiles para ir ejecutando la creación y agregación de otros datos por separado,
    #ya que son funciones separadas
    while True : 
        try: 
            nombre = input('Digite el nombre del alumno -> ')
            numeroRegistro = int(input('Digite el número de registro del alumno -> '))
            alumno = a(nombre = nombre, numeroRegistro = numeroRegistro)
        except :
            print('Error, vuelva a intentarlo')
        else :
            break

    while True :
        try :
            edad = int(input('Digita la edad del alumno -> '))
            alumno.setAge(edad=edad)
        except :
            print('Error, vuelva a intentarlo')
        else :
            break

    while True :
        try :
            nota = input('Digite las notas separandolas por coma -> ')
            alumno.setNota(nota=nota)
        except :
            print('Error, vuelva a intentarlo')
        else :
            break

    print('Datos finales del alumno')
    ddisplay = alumno.detailDisplay()
    
    print(ddisplay)

if __name__ == '__main__' :
    main()