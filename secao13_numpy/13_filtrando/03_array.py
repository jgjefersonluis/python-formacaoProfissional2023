import numpy
array = numpy.array([1,-1,-3,0,6,3,-78])
array_find = numpy.where( (array > 0) & (array < 10) ) 
print(array_find)
