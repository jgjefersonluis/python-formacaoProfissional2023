# 2 - Cria uma função iterável que receba uma lista de números e que retorne 
# a cada iteração um item dessa lista multiplicado por dois.

def duplicado(lista):
  for i in lista:
    yield i*2

lista = [1,2,3,4,5]

for i in duplicado(lista):
  print(i)
  