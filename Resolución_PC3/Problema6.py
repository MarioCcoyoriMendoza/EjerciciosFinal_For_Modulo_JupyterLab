#---------------------------------- Problema 6: --------------------------------
# Escribe una función de Python que imprima las primeras n filas del triángulo de Pascal.
# Nota: El triángulo de Pascal es una figura aritmética y geométrica imaginada por primera 
# vez por Blaise Pascal.

def Triangulo_Pascal(n_filas):
    fila = [1]
    cero = [0]

    for i in range (n_filas):
        print(fila)
        fila = [ i + d for i, d in zip(fila + cero, cero + fila)]

Triangulo_Pascal(4)
