import re
texto = 'existem 64 predios com 700 metros'
info = re.search("^existem", texto)
if info !=None:
  print("Encontrado ocorrencia em ", info.span())
  print("O que foi encontrado: ", info.group())
