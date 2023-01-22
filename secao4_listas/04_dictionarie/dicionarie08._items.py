
idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
lista = idades.items()
print(lista, end='\n\n')
for item in lista:
  print(item[0], item[1])
  