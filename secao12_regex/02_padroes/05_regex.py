import re
texto = 'existem 64 predios com 700 metros'
info = re.search('predios',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
