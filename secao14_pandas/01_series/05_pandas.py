import pandas as pd
minha_serie = pd.Series([1,2,3,4,5], dtype='i4', name="Meus números", index=["Um","Dois","Três","Quatro","Cinco"])
minha_serie['Seis'] = 6
print(minha_serie)
