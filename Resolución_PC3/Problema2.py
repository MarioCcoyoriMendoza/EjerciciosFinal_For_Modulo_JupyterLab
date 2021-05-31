#---------------------------------- Problema 2: --------------------------------
#Escriba una función la cual recibe un string y lo retorna convirtiendo la primera letra de cada palabra 
#a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres.  Precondición: 
#el separador de palabras es el espacio: " ".

def titulo(cadena):
    nueva=" "
    inicioPalabra=True              #indica el inicio de una palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter.lower()
    return nueva
texto = input ('Ingrese el texto: ')
resultado = titulo(texto)
print(f'El título es : {resultado}')