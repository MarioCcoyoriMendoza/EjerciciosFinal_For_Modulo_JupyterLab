######################        PROBLEMA 13          ###########################
#Escriba un programa para imprimir una lista específica después de eliminar los elementos que
#se encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']

lista = ['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
P_0 = lista[0]
P_4 = lista[4]
P_5 = lista[5]
lista.remove(P_0)
lista.remove(P_4)
lista.remove(P_5)
print(lista)