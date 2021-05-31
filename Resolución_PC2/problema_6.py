#---------------------------------- Problema 6: --------------------------------
#Escriba un programa Python que acepte una cadena y calcule el número de dígitos y letras.
#Ejemplo: Python 3.2
#Resultado esperado:
#Letras 6
#dígitos 2
def Contar_digitosyletras(cadena):
    digitos = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras

texto = input ('Ingrese el texto: ')
resultado = Contar_digitosyletras(texto)

print('Cantidad de digitos: %i' % resultado[0])
print('Cantidad de letras: %i' % resultado[1])