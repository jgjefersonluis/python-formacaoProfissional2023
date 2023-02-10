import numpy
array = numpy.array([1,0,1,1,1,0,2])
filtered_array = numpy.array([i for i in array if i ==0 ])
print(filtered_array)
