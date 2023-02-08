'''
3 - Faça uma expressão regular para validar se uma string dada é um dia da 
semana. As possibilidades são:
Segunda-Feira
Terça-Feira
Quarta-Feira
Quinta-Feira
Sexta-Feira
Sábado
Domingo
'''

import re
texto = 'Terça-Feira'
info = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$', texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")
  