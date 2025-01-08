###Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
def leer_tabla():
    numero = int(input('Introduzca un número entero entre 1 y 10: '))
    if 1 <= numero <= 10:
        nombre_fichero = (f'tabla{numero}txt')
        try:
            # Abrir el fichero en modo lectura
            file = open(nombre_fichero, 'r')
            # Leer y mostrar el contenido del fichero
            print('Contenido del fichero:')
            print(file.read())
            # Cerrar el fichero
            file.close()
        except FileNotFoundError:
            # Si el fichero no existe
            print(f"El fichero '{nombre_fichero}' no existe.")
    else:
        print('Número fuera del rango permitido. Introduzca un número entre 1 y 10.')

# Llamar a la función
leer_tabla()