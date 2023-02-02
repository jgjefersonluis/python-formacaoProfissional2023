def anos():
  for i in range(2020,2030):
    yield str(i)

letras = '-'.join(anos())
print(letras)
