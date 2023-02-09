import numpy as np
array = np.array([i for i in range(0,27)])
print(array)
array = array.reshape(3,9)
print(array)
array = array.reshape(9,3)
print(array)
array = array.reshape(3,3,3)
print(array)
