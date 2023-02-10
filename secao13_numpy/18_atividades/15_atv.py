# 15.Crie uma função que diga se um array possui números negativos

import numpy

def tem_negativo(arr):
  return numpy.any(arr <0)

array = numpy.array([4,-5,6,7,8])
print(tem_negativo(array))
