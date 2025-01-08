###Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa debe  incorporar funciones para crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
texto = ('listin' + 'txt')
dicti = {}
def cargar_listin():
    try:
        with open(texto, 'r') as file:
            for linea in file:
                nombre, tlf = linea.strip().split(':')
                dicti[nombre] = tlf
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos vacío
        with open(texto, 'w') as file:
            pass
def creacion():
    Nombre = input('Introduzca el nombre del cliente')
    if Nombre in dicti:
        print ('Este nombre ya esta incluido en el fichero')
        with open(texto, 'a') as file:
            file.write(f"{Nombre}:{tlf}\n")
        print('Cliente añadido al fichero.')
    else:
        tlf = input('Introduzca el número de teléfono: ')
        dicti[Nombre] = tlf
    

def eliminar():
    nombre_del_usuario = input('Introduzca el nombre que quiere eliminar de la lista')
    if nombre_del_usuario in dicti:
        del dicti[nombre_del_usuario]
        with open(texto, 'w') as file:
            for nombre, telefono in dicti.items():
                file.write(f"{nombre}:{telefono}\n")
        print(f"Cliente '{nombre_del_usuario}' eliminado del fichero.")
    else:
        print('No existe el nombre en el listín.')
cargar_listin()
creacion()
eliminar()

