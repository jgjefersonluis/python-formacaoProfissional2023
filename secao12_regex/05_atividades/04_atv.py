# 4 - Faça uma expressão regular para detectar telefones que comecem com 95. 
# Telefones que começam com 95 devem ser bloqueados. Um número de 
# telefone deve ser válido para poder ser validado, na forma XXXXXXXX onde X é 
# um número. Primeiro diga se é um número válido.
# Caso seja diga se ele foi bloqueado ou não.

import re
texto = '9645634'

info = re.search("^([0-9]{8})$", texto)

if info !=None:
  print("Número válido")
  info2 = re.search("^95([0-9]{6})$", texto)
  if info2 !=None:
    print("Telefone bloqueado")
  else:
    print("Telefone não bloqueado")
else:
  print("Número inválido")
  