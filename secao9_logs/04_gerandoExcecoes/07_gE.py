lista = [1]
try:
  print(lista[10])
except IndexError as error:
  raise error
  