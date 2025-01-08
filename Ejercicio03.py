###Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def tabla_multiplicar(): 
    Numero = int(input('Introduzca un número del 1 al 10: ')) 
    M = int(input('Introduzca la línea que quiera leer del fichero: ')) 
    if Numero < 1 or Numero > 10 or M < 1 or M > 10:
        print("Los números deben estar entre 1 y 10.")
        return
    texto = 'tabla' + str(Numero) + '.txt'
    try:
        file = open(texto, 'r')
    except FileNotFoundError:
        print(f"El fichero '{texto}' no existe. Creando el archivo...")
        file = open(texto, 'w')
        n = 1
        while n <= 10:
            Operacion = f"{Numero} x {n} = {Numero * n}"
            file.write(Operacion + '\n')
            n += 1
        file.close()
        file = open(texto, 'r')  
    lineas = file.readlines()
    file.close()
    if M <= len(lineas):
        print(f"Línea {M}: {lineas[M - 1].strip()}")
    else:
        print(f"El fichero '{texto}' no tiene tantas líneas.")
tabla_multiplicar()
