import pandas as pd
import numpy as np
array = np.array([45.4,50.5, 65.7, 98.7])
pesos = pd.Series(array, index=['Carlos',"josé","Maria","Fernanda"])
print(pesos)
print(type(pesos))
