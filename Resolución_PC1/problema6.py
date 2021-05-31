##################        PROBLEMA6          ############################
#Escribir un programa que le solicite al usuario su edad y la guarde en una variable. Que luego
#solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable.Finalmente, 
#mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años 
#y además compró más de 1 artículo.

Edad=int(input("Ingrese la edad del usuario : "))
N_Artigulos=int(input("Ingrese la cantidad de articulos a comprar : "))
Valor=str(Edad>18 and N_Artigulos>1)
print(f"{Valor}")