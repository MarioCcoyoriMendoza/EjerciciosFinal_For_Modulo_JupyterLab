#---------------------------------- Problema 2: --------------------------------
#Escriba un programa en Python para construir el siguiente patrón, usando un bucle for
#anidado
#(El tipo range() con un único argumento se escribe range(n) y crea una lista inmutable 
#de n números enteros consecutivos que empieza en 0 y acaba en n - 1.
#>>> x = range(10)
#>>> x
#range(0, 10)
#>>> list(x)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#(El tipo range con dos argumentos se escribe range(m, n) y crea una lista inmutable 
#de enteros consecutivos que empieza en m y acaba en n - 1.
#>>> list(range(5, 10))
#[5, 6, 7, 8, 9])
#El tipo range con tres argumentos se escribe range(m, n, p) y crea una lista inmutable de enteros 
#que empieza en m y acaba justo antes de superar o igualar a n, aumentando los valores de p en p. Si p 
# es negativo, los valores van disminuyendo de p en p.
#>>> list(range(5, 21, 3))
#[5, 8, 11, 14, 17, 20]
#>>> list(range(10, 0, -2))
#[10, 8, 6, 4, 2]
N = int(input('Ingrese la altura del triangulo: '))
for i in range(1, N + 1 ):
    print(' *' * i)
#Triangulo Rectangulo
#*
#* *
#* * *
for i in range(N-1, 0 ,-1):
    print(' *' * i)


