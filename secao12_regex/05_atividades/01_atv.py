# 1 - Faça uma expressão regular para reconhecer números de 20 até 35 apenas.
# O texto deve ser composto apenas destes números, nenhum outro caractere 
# é permitido

import re
texto = '16'
info = re.search("^([2][0-9])|([3][0-5])$", texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")
  