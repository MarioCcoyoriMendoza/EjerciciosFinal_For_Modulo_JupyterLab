#---------------------------------- Problema 1: --------------------------------
#Escriba una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras 
#están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado 
#por parámetro.
def longitud_última_palabra (cadena):
    letras = 0
    for c in cadena:
        if c.isalpha():
            letras +=1
        else:
            pass
    return letras

texto = input ('Ingrese el texto: ')
resultado = longitud_última_palabra(texto)
print('La longitud de la ultima palabra es : {}'.format(resultado[1]))