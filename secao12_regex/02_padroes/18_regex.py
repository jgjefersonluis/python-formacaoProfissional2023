import re
texto = 'aaaaaa'
info = re.search('^(aa){2,3}$',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  