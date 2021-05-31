######################        PROBLEMA8          ############################
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
#divisor es cero el programa debe mostrar un error.
a=float(input("Ingrese el numerador: "))
b=float(input("Ingrese el denominador: "))
división=float(a/b)
if b!=0:
    print(f"El resultado de la división es: {división}")
else: 
    print("Vuelva a ingresar los números")