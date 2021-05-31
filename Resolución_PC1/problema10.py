########################        PROBLEMA 10          ############################
#Escribí un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe
#ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

año=int(input("Ingrese el año : "))
if año % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")