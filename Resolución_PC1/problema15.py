######################        PROBLEMA 15         ############################
#Escriba un programa Python para mover un elemento específico en una lista dada.
#Lista original:
#['rojo', 'verde', 'blanco', 'negro', 'naranja']
#Mueva el blanco al final de dicha lista:
#['rojo', 'verde', 'negro', 'naranja', 'blanco']

colores = ['rojo', 'verde', 'blanco', 'negro', 'naranja']
print("Lista original:")
print(colores)
el = "blanco"
print("Mover",el,"al final de la lista:")
colores.append(colores.pop(colores.index(el)))
print(colores)
colors = ['rojo', 'verde', 'blanco', 'negro', 'naranja']
print("\nLista original:")
print(colores)
el = "rojo"
print("Mover",el,"al final de la lista:")
colores.append(colores.pop(colores.index(el)))
print(colores)
colors = ['rojo', 'verde', 'blanco', 'negro', 'naranja']
print("\nLista original:")
print(colores)
el = "negro"
print("Mover",el,"al final de la lista:")
colores.append(colores.pop(colores.index(el)))
print(colores)