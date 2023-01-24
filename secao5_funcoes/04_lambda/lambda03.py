def multiplica(y):
  return lambda x : x * y

valor = multiplica(2)

resultado = valor(10)

print(resultado)
