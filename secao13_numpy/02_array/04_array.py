"""i = inteiro
b = booleano
u = inteiro sem sinal
f = ponto flutuante
S = String (bytes)
U = String Unicode
"""

import numpy
array = numpy.array(["abc","def","ghi"], dtype= 'S3')
print(array)
print(array.dtype)
print(array.itemsize)
print(array.nbytes)
