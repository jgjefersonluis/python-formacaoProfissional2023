
import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb){2}',texto)
if info != None:
  print('Encontrado ocorrĂȘncia em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  