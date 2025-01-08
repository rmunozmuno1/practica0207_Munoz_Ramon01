### Escribir un programa que acceda al fichero de internet mediante la url indicada y muestre por pantalla el número de palabras que contiene.
import urllib
def arch():
    try:
        file = urllib.request.urlopen('http://textfiles.com/adventure/aencounter.txt')
        words = 0
        for line in file:
            decoded_line = line.decode("utf-8")
            palabras_de_la_pagina = decoded_line.split()
            words += len(palabras_de_la_pagina)
        print (f"Contiene {words} palabras")
    except:
        print ('Error introduzca una URL valida')
arch()