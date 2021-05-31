#---------------------------------- Problema 4: --------------------------------
#Escriba un programa Python que imprima cada elemento y su tipo correspondiente de la siguiente lista.
#Lista de muestra:
#[1452, 11.23, 1 + 2j, True, 'Python', (0, -1), [5, 12], {"Clase": 'V', "Seccion": 'A'} ]

lista_combinada= [1452, 11.23, 1 + 2j, True, 'Python', (0, -1), [5, 12], {"Clase": 'V', "Seccion": 'A'} ]
for i in range(len(lista_combinada)):
    print('valor de elemento : {} y Tipo de dato {}'.format(lista_combinada[i], type(lista_combinada[i])))
