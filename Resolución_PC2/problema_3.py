#---------------------------------- Problema 3: --------------------------------
#Escriba un programa en Python para contar la cantidad de números pares e impares de una
#serie de números.
def contar_pares_impares(lista):
    pares, impares = 0,0

    for n in lista:
        if n % 2 ==0:
            pares +=1
        else:
            impares +=1
    return pares, impares

numeros = [1,2,3,4,5,6,7,11,13]
resultado = contar_pares_impares(numeros)
#Forma 3
print(numeros)
print(f'La cantidad de pares es: {resultado[0]}')  
print(f'La cantidad de impares es: {resultado[1]}')  
print()
#Forma 2
print(numeros)
print('La cantidad de pares es: %i' % resultado[0])
print('La cantidad de impares es: %i' % resultado[1])
print()
#Forma 3
print(numeros)
print('La cantidad de pares es: {}'.format(resultado[0]))
print('La cantidad de impares es: {}'.format(resultado[1]))
print()


