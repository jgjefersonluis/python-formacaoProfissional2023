def printa_positivo(numero):
  assert(numero >=0)
  print(numero)

try:
  printa_positivo(-1)
except AssertionError as erro:
  print("O erro é ", str(erro))
except Exception as erro1:
  print("Erro qualquer> ", str(erro1))
  