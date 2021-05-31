#---------------------------------- Problema 7: --------------------------------
#Escribe una función de Python para multiplicar todos los números en una lista.
#Lista de muestra: [8, 2, 3, -1, 7]
#Resultado esperado: -336
def multiplicar(N):
    producto = 1
    
    for i in N:
        producto *= i
    
    return producto
lista_N = [8, 2, 3, -1,7]
print(type(lista_N))
print(multiplicar(lista_N))

