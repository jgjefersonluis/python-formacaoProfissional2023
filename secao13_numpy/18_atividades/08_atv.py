# 8. Crie uma matriz 3x3 aleatória. Percorra linha por linha com um laço e 
# imprima a soma de cada linha.

import numpy
array = numpy.random.randint(1,50,(3,3))
print(array)
for linha in array:
  print(numpy.sum(linha))
  