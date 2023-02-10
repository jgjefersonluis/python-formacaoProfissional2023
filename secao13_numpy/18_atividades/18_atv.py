# 18.Crie uma função que ordene uma matriz e remova todos os números impares.

import numpy

def ordena_pares(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return arr[filter]

array = numpy.random.randint(0,10,(100))  
print(ordena_pares(array))

