# 7.Gere uma array 3x3 com números inteiros aleatórios entre 5 e 20. 
# Então imprima a primeira coluna e última linha

import numpy
array = numpy.random.randint(5,20,(3,3))
print(array)
print(array[:,0])
print(array[2,:])
