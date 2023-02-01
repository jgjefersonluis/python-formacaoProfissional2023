print("Inicio")
lista = [1,2,3]
try:
  numero = int('b')
except Exception as error:
  print("Falha no cast: ", str(error))
