import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12 = np.concatenate((array1,array2),axis=0) 
print(array12)
array12 = np.concatenate((array1,array2),axis=1) 
print(array12)
