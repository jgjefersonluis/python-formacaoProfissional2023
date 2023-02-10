import numpy
array = numpy.array([1,0,1,1,1,0,2])
filter = (array ==1) | (array ==2)
filter_array = array[filter]
print(filter_array)
