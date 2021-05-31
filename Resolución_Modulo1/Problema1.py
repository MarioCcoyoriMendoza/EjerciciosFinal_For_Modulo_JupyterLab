# python hello.py
N = int(input('Ingrese la altura del triangulo: '))
if  N > 0 and N<=8:
    for i in range(1,N+1):
        print((N-i) * '  ' + i * ' #' )
else:
    print("Vuelva a ingresar la altura del triangulo ")

