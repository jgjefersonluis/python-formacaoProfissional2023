import numpy
tipo_pessoa = numpy.dtype([ ('nome','S10'),('idade','i4')  ] )  
array = numpy.array([ ('Rodrigo',24), ('fernando',45) ], dtype= tipo_pessoa)
print(array)
print(array.ndim)
print(array.size)
print(array.shape)
print(array.dtype)
print(array.itemsize )
print(array.nbytes)
