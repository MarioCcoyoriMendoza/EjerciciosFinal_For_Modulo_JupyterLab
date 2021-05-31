import random
def adivina_numero():
    suerte = random.randint(0, 100)
    x=int(input("Ingrese el numero entre 0 a 100 "))
    while (x != suerte):
        if x<suerte:
            print("El numero aleatorio es superior al numero elegido")
            x = int(input("Ingrese el número entre 0 a 100 "))
        else:
            print("El numero aleatorio es inferior al numero elegido")
            x = int(input("Ingrese el número entre 0 a 100 "))

    print("Felicidades, HA GANADO") 

