from math import sqrt
#Establecemos los valores de "a", "b", "c"
a=float(input("Ingrese el coeficiente a : "))
b=float(input("Ingrese el coeficiente b : "))
c=float(input("Ingrese el coeficiente c : "))
x1= (-b + sqrt(b**2-4*a*c ))/2*a
x2= (-b - sqrt(b**2-4*a*c ))/2*a

if b**2-4*a*c > 0:
    print(f"La primera solución es: {x1}")
    print(f"La segunda solución es: {x2}")
elif b**2-4*a*c == 0:
    print(f"La solución unica es: {x2}")
else:
    print("La solución no es real")
 
 