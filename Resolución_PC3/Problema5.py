#---------------------------------- Problema 5: --------------------------------
# Escriba una función que reciba un string, la función debe devolver un substring que cumpla las 
# siguientes condiciones:
#• El substring debe ser la más larga de todas los posibles substrings en el string dado.
#• No debe haber caracteres repetidos en el substring.
#• Si hay más de un substring que satisfaga las dos condiciones anteriores, imprima el substring que aparece primero.
#• Si no hay ningún substring que satisfaga todas las condiciones antes mencionadas, imprima -1.
#Ejemplo:
#String: “caracter”
#Resultado esperado: “racte”

def retorno_caracter(texto):
    sub=[]
    lista =[]
    lista2 = []
    longitud=[]
    lista3 =[]
    valor = 1
    listafinal =[]
    listadofinal2 =[]
    for i in range(len(texto),0,-1):
        sub = texto[0:i]
        #print(sub)
        for j,l in enumerate(sub):
            if sub[j+1:].count(l)>0:
                valor = valor * 0
        if valor == 1:
            lista.append(sub)        
        #print(valor)
        valor = 1
            
    for i in range(0,len(texto),1):
        sub = texto[i:len(texto)]
        #print(sub)
        for j,l in enumerate(sub):
            if sub[j+1:].count(l)>0:
                valor = valor * 0
        if valor == 1:
            lista.append(sub)        
        #print(valor)
        valor = 1    

    for i in range(0,len(texto),1):
        for k in range(0,len(texto),1):
            sub = texto[i:len(texto)-k]
            #print(sub)
            for j,l in enumerate(sub):
                if sub[j+1:].count(l)>0:
                    valor = valor * 0
            if valor == 1:
                lista.append(sub)        
            #print(valor)
            valor = 1    
    for i in range(0,len(texto),1):
        for k in range(0,len(texto),1):
            sub = texto[k:len(texto)-i]
            #print(sub)
            for j,l in enumerate(sub):
                if sub[j+1:].count(l)>0:
                    valor = valor * 0
            if valor == 1:
                lista.append(sub)        
            #print(valor)
            valor = 1    

    for item in lista:
        if item not in lista2:
            lista2.append(item)
    for i in range(len(lista2)):
        longitud.append(len(lista2[i]))
    maximo =max(longitud)
    for i in range(len(longitud)):
            if(longitud[i] == maximo):
                lista3.append(i)
    for i in range(len(lista3)):
        listafinal.append(lista2[lista3[i]])
    for i in range(len(listafinal)):
        listadofinal2.append(texto.index(listafinal[i]))
    valorfinal= listafinal[listadofinal2.index(min(listadofinal2))]
    pass
    return valorfinal

#ejemplo:
texto = "caracter"
resultado = retorno_caracter(texto)
print("El resultado es: " + resultado)