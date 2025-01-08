###Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido
def tabla_multiplicar():
    Numero = int(input('Introduzca un numero del 1 al 10'))
    n = 0
    texto = ('tabla' + str(Numero) + 'txt')
    file = open(texto, 'w')
    while n <= 10:
        Operacion = str(Numero * n)
        n = n + 1
        file.write (Operacion + '\n')
    file.close
tabla_multiplicar()


