#---------------------------------- Problema 11: --------------------------------
#Escriba una función de Python que devuelva los números pares de una lista dada.
#Lista de muestras: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Resultado esperado: [2, 4, 6, 8]
def devolver_pares(numeros):
    numeros_pares = []
    for n in numeros:
        if n % 2 ==0:
            numeros_pares.append(n)
    return numeros_pares

numeros = [1,2,3,4,5,6,7,8,9]
resultado = devolver_pares(numeros)

print(f'La lista inicial dada es : {numeros}')
print(f'Los numeros pares son : {resultado}')
