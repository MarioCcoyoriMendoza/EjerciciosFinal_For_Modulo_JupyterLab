##################        PROBLEMA4          ############################
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
#venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
#calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
#payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y
#muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

a=int(input("Ingrese el número de payasos pedidos : "))
b=int(input("Ingrese el número de muñecas pedidos : "))
PesoTotal=a*112+b*75
print(f"El número de payasos vendidos es : {a}")
print(f"El número de muñecas vendidas es : {b}")
print(f"El peso total es : {PesoTotal}")