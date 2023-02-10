import numpy
array = numpy.array([1,0,1,1,1,0,0])
filter = array ==1
filter_array = array[filter]
print(filter_array)
