import numpy as np
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
array12 = np.concatenate((array1,array2),axis=0)
print(array12)
