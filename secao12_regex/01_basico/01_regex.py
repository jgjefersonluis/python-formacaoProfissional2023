import re
texto = '00123451'
info = re.search('1',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  