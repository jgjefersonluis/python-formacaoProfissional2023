import re
texto = '99224566'

info = re.search('^99([0-9]{6})$', texto)

if info != None:
  print("Número válido")
else:
  print("Número inválido")
  