import re

texto = '01234 ABC'

info = re.search("\s+",texto)

if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())
  