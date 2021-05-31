##################        PROBLEMA5          ############################
#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después
#muestre en pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros
#enteros positivos puede ser calculada de la siguiente forma:

N=int(input("Ingrese el número entero positivo: "))
Suma=int((N*(N+1))/2)
if N>0:
    print(f"El peso total es : {Suma}")
else:
    print("El número entero no es positivo")
