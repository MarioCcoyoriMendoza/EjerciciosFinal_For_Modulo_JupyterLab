#---------------------------------- Problema 10: --------------------------------
#Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no.
def primo(Numero):
    if Numero == 1:
        return False
    elif Numero == 2:
        return True
    else:
        for i in range (2, Numero ):
            if Numero % i == 0:
                return False
        return True

for i in range (1, 101):
    print(i, primo(i))
