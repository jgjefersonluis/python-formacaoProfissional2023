data

print(data.loc['Roger']['Idade'])
print(data.loc['Roger'][0])

print(data.iloc[0]['Idade'])
print(data.iloc[0][0])

print(data.loc['Roger'])
print(type(data.loc['Roger']))

print(data.iloc[0])

data.loc['Cristiano':'Jeferson'] #slicing

data.iloc[1:4]

print(data['Idade'])

idade = data['Idade']
print(idade[3])
print(idade['Diego'])

data[['Idade','Altura']]

colunas = data[['Idade','Altura']]
print(type(colunas))

data

colunas = data.iloc[:,1:3]
colunas

colunas = data.loc[:,"Idade":"Profissão"]
colunas
