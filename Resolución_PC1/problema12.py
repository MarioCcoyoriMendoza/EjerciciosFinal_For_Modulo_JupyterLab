######################        PROBLEMA 12          ############################
#Escriba un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa',
#'a', 'día', 'buen', 'Di'].
numero = int(input("Número de palabras que tiene la lista: "))
if numero < 1:
    print("¡Invalido!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    inversa = []
    for i in lista:
        inversa = [i] + inversa
    print("La lista inversa es:", inversa)