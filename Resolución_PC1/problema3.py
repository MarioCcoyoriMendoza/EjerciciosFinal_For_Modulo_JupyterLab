##################        PROBLEMA3          ############################
#Escribir un programa que solicite al usuario ingresar un número con decimales y almacénalo en
#una variable. A continuación, el programa debe solicitar al usuario que ingrese un número
#entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de
#la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla
#el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado
#de la operación.

a=float(input("Ingrese el número en decimales: "))
b=int(input("Ingrese el número entero: "))
suma=(a+b)
print(f"El resultado de la suma es : {suma}")
