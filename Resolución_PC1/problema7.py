######################        PROBLEMA7          ############################
#Escribe un programa que solicite al usuario el ingreso de dos números diferentes y muestre en
#pantalla al mayor de los dos.

a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
if a>b:
    print(f"{a}")
elif b>a:
    print(f"{b}")
else:
    print("Vuelva a ingresar los números")



