#---------------------------------- Problema 3: --------------------------------
#Escriba una función que acepte una secuencia de palabras separadas por guiones como entrada e imprima 
#las palabras en una secuencia separada por guiones después de ordenarlas alfabéticamente.

def orden_alfabético(texto):
    secuencia=texto.sort()
    return secuencia

entrada = input ('Escriba una secuencia de palabras separadas por guiones : ')
lista = entrada.split('-')
resultado = orden_alfabético(lista)
print(lista)
StrA = '-'.join(lista)
print(StrA)




