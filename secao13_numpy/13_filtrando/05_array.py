import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.any((array>0) & (array<10))
print(array_find)
