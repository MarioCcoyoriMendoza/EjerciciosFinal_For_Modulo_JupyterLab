m = float(input('Ingrese cantidad de dinero depositada en la cuenta de ahorros:' ))
## m es el ahorro inicial
## si el interes es 4% <> 1.04 * m 
## range (1,6) hasta el quinto año
for a in range(1,6):
    m = m * 1.04 
    print(f"El monto al final del año {a} es :{round(m,2)}")
    