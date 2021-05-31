import problema10.operaciones as op

num_uno,num_dos = op.entradas()

print("{} + {} = {}".format(num_uno,num_dos,op.suma(num_uno, num_dos)))
print("{} - {} = {}".format(num_uno,num_dos,op.resta(num_uno, num_dos)))
print("{} * {} = {}".format(num_uno,num_dos,op.producto(num_uno, num_dos)))
print("{} / {} = {}".format(num_uno,num_dos,op.división(num_uno, num_dos)))