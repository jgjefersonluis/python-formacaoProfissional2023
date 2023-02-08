# 2 - Faça uma expressão regular para dizer se a palavra 'python' esta na frase.

import re
texto = 'este notebook utiliza python'
info = re.search("python", texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")
  