import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12r = np.vstack((array1,array2))
array12c = np.hstack((array1,array2))
print(array12r)
print(array12c)
