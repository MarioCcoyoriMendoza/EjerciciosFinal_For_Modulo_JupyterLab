#---------------------------------- Problema 1: --------------------------------
#Escribe un programa en Python para encontrar los números que son divisibles por 7 y
#múltiplos de 5, entre 1500 y 2700 (ambos incluidos).
resultado=[]
for n in range(1500,2700+1):
    if n % 5 == 0 and n % 7 == 0:
        resultado.append(n)
print(resultado)


