def print_str(texto, indice):
  if indice == len(texto):
    return
  print(texto[indice])
  print_str(texto, indice + 1)

print_str("Python",0)
