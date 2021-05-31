##################        PROBLEMA1          ############################
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el
#usuario lo introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es
#el nombre que el usuario haya introducido.


# Esto imprime "Hola, nombre!"
nombre=str(input("Introduzca su nombre: "))
#Place horder se llenan los parametros de format
#forma1
print(f"Hola, {nombre}!")   
#forma2
print("Hola, %s!" %nombre)
#forma3
print("Hola, {}!".format(nombre))