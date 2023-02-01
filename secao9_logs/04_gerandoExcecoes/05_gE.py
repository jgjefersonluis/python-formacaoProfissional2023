def printa_positivo(numero):
  if numero < 0:
    raise ValueError("Valor não pode ser negativo")
  print(numero)

try:
  printa_positivo(-1)
except ValueError as erro:
  print("O erro é ", str(erro))
except Exception as erro1:
  print("Erro qualquer> ", str(erro1))
  