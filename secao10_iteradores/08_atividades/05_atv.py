# 5 - Utilizando como base o exercício 1, retorne o número que representa o mês 
# e o próprio mês. Faça isso de duas maneiras diferentes 
# (usando enumeradores e a outra usando join).

def meses_enum():
  meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
  for i in enumerate(meses):
    yield i

for indice, mes in meses_enum():
  print(indice+1, mes)
  