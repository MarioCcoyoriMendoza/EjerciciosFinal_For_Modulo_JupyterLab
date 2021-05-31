#---------------------------------- Problema 9: --------------------------------
#Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos
#únicos de la primera lista.
def elementos_unicos (lista):
    conjunto=set(lista)
    return conjunto
lista_inicial = ['a','b','c','d','e','f','b','d']
lista_unica = elementos_unicos(lista_inicial)
print(lista_inicial)
print(lista_unica)