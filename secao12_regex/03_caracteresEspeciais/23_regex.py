import re

texto = '01234 ABC'

info = re.search("\W",texto)

if info != None:
  print("Encontrada ocorrĂȘncia em ", info.span())
  print("O que foi encontrado ", info.group())