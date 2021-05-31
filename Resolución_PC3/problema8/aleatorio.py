import random
def numero_aleatorio():
    lista =[]
    for i in range(0,20):
        lista.append(random.randint(0, 100))
    lista.sort()
    print(lista)


