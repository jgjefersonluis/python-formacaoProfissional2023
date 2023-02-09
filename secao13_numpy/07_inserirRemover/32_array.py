import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = np.append(array,[[10,11,12]], axis=0) #linha
array2 = np.append(array,[[10],[11],[12]], axis = 1) #adicionado por coluna
print(array, end='\n\n')
print(array1, end='\n\n')
print(array2, end='\n\n')
