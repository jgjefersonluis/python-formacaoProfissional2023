import re
texto = '0 C°'

info = re.search('^(-)?[0-9]+ C°$', texto)

if info != None:
  print("Temperatura válida")
else:
  print("Temperatura inválida")
  