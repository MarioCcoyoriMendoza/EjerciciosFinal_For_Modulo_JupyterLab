#---------------------------------- Problema 12: --------------------------------
#Escribe una función de Python para calcular el factorial de un número (un entero no negativo).
#La función acepta el número como argumento.
def factorial(n):
    if n>= 0:
       producto = 1
       for i in range (1, n + 1):
         producto *= i
       return producto
    else:
        print('Vuelva a ingresar el parametro')

print('El {:d}! es igual a {:d}'.format(8, factorial(8)))
