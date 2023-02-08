import re
texto = "Texto teste"

info = re.search('(^[A-Za-z]+ +[A-Za-z]+ *$)', texto)
if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Padrão não encontrado")

  