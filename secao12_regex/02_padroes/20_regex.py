import re
texto = 'Olá sou eu, AQUI, e nada para frente'
info = re.search('(.)*(AQUI)(.)*',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")
  