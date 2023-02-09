import numpy as np
array = np.array([[1,2,3],[7,8,9],[10,11,12]])
array1 = np.insert(array,1,[4,5,6], axis = 0)
array2 = np.insert(array,1,[4,5,6], axis = 1)
print(array1, end='\n\n')
print(array2, end='\n\n')
