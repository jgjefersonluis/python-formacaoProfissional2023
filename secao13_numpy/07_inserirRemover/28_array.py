import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
array[0] = [1,2,4]
array[1,1:3] = [0,0]
array[0,0] = 10
print(array)
