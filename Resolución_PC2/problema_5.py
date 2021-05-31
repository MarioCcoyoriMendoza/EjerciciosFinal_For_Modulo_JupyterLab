#---------------------------------- Problema 5: --------------------------------
#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
serie_de_Fibonacci= []
a , b = 0 , 1
while b < 50 :
    serie_de_Fibonacci.append(b)
    a,b = b, a + b
print(serie_de_Fibonacci)
