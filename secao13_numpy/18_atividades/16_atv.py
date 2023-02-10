# 16.Crie uma função que remova os números negativos de uma array.

import numpy
def tira_negativo(arr):
  filter = arr >=0
  return arr[filter]

array = numpy.array([1,-5,5,4,3,-2,-1])
print(tira_negativo(array))
