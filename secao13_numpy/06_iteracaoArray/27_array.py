import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(array, order='F'):
  print(x)
  