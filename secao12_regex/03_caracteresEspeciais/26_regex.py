import re

texto = '01234 ABC'

info = re.search("\S+",texto)

if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())
  