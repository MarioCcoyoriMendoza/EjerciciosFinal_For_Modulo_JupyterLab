#---------------------------------- Problema 10: --------------------------------
# Crea el siguiente módulo:
# El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto 
# y una división entre dos números. Todas ellas devolverán el resultado. En las funciones del módulo deberá de 
# haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso 
# incluye:
# • En caso de que se envíen valores a las funciones que no sean números, deberá aparecer un mensaje que informe 
# Error: Tipo de dato no válido.
# • En caso de realizar una división por cero, deberá aparecer un mensaje que informe Error: No es posible 
# dividir entre cero.
# Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás importar el 
# módulo y ejecutar las funciones.

def suma(num_uno, num_dos):
    resultado = num_uno + num_dos
    return resultado

def resta(num_uno, num_dos):
    resultado = num_uno + num_dos
    return resultado

def producto(num_uno, num_dos):
    resultado = num_uno*num_dos
    return resultado

def división(num_uno, num_dos):
    if num_dos != 0:
        resultado = num_uno/num_dos
    else:
        print('No es posible dividir un número entre cero')
    return resultado

def entradas():
    num_uno = int(input("Ingrese el primer número:"))
    num_dos = int(input("Ingrese el primer número:"))
    return num_uno,num_dos

