import re

texto = '01234 ABC'

info = re.search("\d+",texto)

if info != None:
  print("Encontrada ocorrĂȘncia em ", info.span())
  print("O que foi encontrado ", info.group())
  