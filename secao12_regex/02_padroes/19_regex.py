import re
# {,7}  7 ou menos
# {7,}  7 ou mais 
texto = 'xxxxxxxx'
info = re.search('^x{7,}$',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
