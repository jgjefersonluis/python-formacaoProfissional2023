import re
texto = ''
info = re.search('^(aa)?$',texto)
if info != None:
  print('Encontrado ocorrĂȘncia em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  