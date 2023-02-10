import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array1 = numpy.cumprod(array, axis =0)
array2 = numpy.cumprod(array, axis =1)
print(array1)
print(array2)
