import re
texto = 'abbabb'
info = re.search('abb',texto)
if info != None:
  print('Encontrado ocorrĂȘncia em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  