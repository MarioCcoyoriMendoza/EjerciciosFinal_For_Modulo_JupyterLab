#---------------------------------- Problema 4: --------------------------------
#Escriba una función que acepte dos listas y devuelva True si los elementos de una lista son cuadrados 
#de los elementos de la otra lista e independientemente del orden, en caso contrario devuelva False.
#Ejemplo:
# a = [121, 144, 19, 3, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 9, 361, 20736, 361] 
# Resultado esperado: True
import math
def verificar_cuadrados(lista):
    for n in lista:
        if n>0:
            print('El número es positivo')
            r=math.sqrt(n)
            if  r % 1 == 0:
                valor=str(r % 1 == 0)
        else:
            print('El número no negativo')
    return print(f'{valor}')

lista_a = [121, 144, 19, 3, 19, 144, 19, 11]
lista_b = [121, 14641, 20736, 361, 9, 361, 20736, 361] 
print(f'La lista_b {lista_b} es el cuadrado de la lista_a {lista_a} ? ')
resultado = verificar_cuadrados(lista_b)


