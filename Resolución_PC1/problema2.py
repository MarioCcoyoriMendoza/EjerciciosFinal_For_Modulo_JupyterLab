##################        PROBLEMA2          ############################
#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un
#valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

N=int(input("Ingrese el numero de show musicales asistidos: "))
Valor=str(N>=3)
print(f"{Valor}")
