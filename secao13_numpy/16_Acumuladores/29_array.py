import numpy
array = numpy.array([[1,4,8],[4,3,6]])
print(array)
print(numpy.amin(array))
print(numpy.amin(array, axis = 1))
print(numpy.amin(array, axis = 0))
