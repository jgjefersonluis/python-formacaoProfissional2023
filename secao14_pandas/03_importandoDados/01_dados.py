import pandas as pd
data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc['Roger']

len(data.columns)

data.columns

len(data.index)

data.index

data.shape

for indice, linha in data.iterrows():
  print(indice, linha[0], linha[1], linha[2])

for coluna in data:
  print(coluna)

data['Altura']

for coluna in data:
  print(data[coluna])
  