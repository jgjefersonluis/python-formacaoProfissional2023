import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb)+',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  