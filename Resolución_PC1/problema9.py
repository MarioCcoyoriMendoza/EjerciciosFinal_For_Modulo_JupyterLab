######################        PROBLEMA 9          ############################
#Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es
#vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle
#que no se puede procesar el dato.

letra=str(input("Ingrese la letra : "))
if letra=="a":
    print("Es vocal")
elif letra=="e":
    print("Es vocal")
elif letra=="i":
    print("Es vocal")
elif letra=="o":
    print("Es vocal")
elif letra=="u":
    print("Es vocal")
elif len(letra)>1:
    print("No se puede procesar el dato ")