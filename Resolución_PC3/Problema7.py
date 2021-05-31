#---------------------------------- Problema 7: --------------------------------
def ruta(direccion):
    while(len(direccion)!= 1):
        for i in range(len(direccion)):
            if direccion[i] =="NORTE" and direccion [i+1] =="SUR":
                direccion.pop(i)
                direccion.pop(i)
                print(direccion)
                break
            elif direccion[i] =="SUR" and direccion [i+1] =="NORTE":
                direccion.pop(i)
                direccion.pop(i)
                print(direccion)
                break
            elif direccion[i] =="ESTE" and direccion [i+1] =="OESTE":
                direccion.pop(i)
                direccion.pop(i)
                print(direccion)
                break
            elif direccion[i] =="OESTE" and direccion [i+1] =="ESTE":
                direccion.pop(i)
                direccion.pop(i)
                print(direccion)
                break
    return direccion

#Ejemplo
direccion = ["NORTE", "SUR", "SUR", "ESTE", "OESTE","NORTE","OESTE"]
resultado = ruta(direccion)
print('La direccion a donde debe ir es: ')
print(resultado)

