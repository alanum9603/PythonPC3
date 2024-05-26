def calculo_nivel_combustible(txt) : 
    try : 
        #Eliminamos los espacios por si hubo un error de este tipo en la digitación
        txt.replace(' ','')
        #Separamos el valor por la '/', pero se guardarán en las variables como cadena 
        X, Y = txt.split('/')
        #Transformamos los valores a entero
        X = int(X)
        Y = int(Y)
        #Realizamos un if para excepciones que no podría detectar el try except, ya que no son errores como tal
        if X > Y :
            print('El dividendo no puede ser mayor al divisor')
            return False, ''
        elif X < 0 :
            print('El número debe ser entero positivo')
            return False, ''
        else :
            return True, nivel_combustible(X, Y)
    except ValueError :
        #Se detecta este error cuando se transforma las variables de X e Y a entero
        print('Formato incorrecto, vuelva a intentarlo')
        return False, ''
    except ZeroDivisionError :
        #Se detecta este error cuando se realiza la división en el método nivel_combustible
        print('El divisor no puede ser cero')
        return False, ''
        

def nivel_combustible(X : int, Y : int) :
    #Se obtiene un valor porcentual
    calculo = (X / Y) * 100 
    res = ''
    #Se realiza un if para verificar que el valor sea superior al 99% sea inferior al 1% o sea superior al 99%, 
    #en tal caso, como en un medidor de gasolina, mostraría 'E' y 'F' respectivamente
    if calculo < 1 :
        res = 'E'
    elif calculo > 99 :
        res = 'F'
    else :
        res = f'{calculo}%' 
    return res