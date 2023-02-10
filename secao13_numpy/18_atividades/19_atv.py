# 19.Realize o mesmo exercício anterior, mas remova valores duplicados.

import numpy

def ordena_pares_unicos(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return numpy.unique( arr[filter])

array = numpy.random.randint(0,10,(100))  
print(ordena_pares_unicos(array))
