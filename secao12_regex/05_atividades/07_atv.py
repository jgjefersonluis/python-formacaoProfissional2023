# 7 (DESAFIO) - Faça uma expressão regular para validar se uma expressão é uma 
# conta matemática valida. Nessa conta matemática só podem haver 2 números 
# inteiros sendo somados ou subtraídos entre si. Valide se é uma expressão 
# matemática ou não.

import re

texto = '3232+4453'
info = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto)
if info != None:
  print("Expressão válida")
else:
  print("Expressão inválida")
  