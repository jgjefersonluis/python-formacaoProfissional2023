# 10 - Crie uma função que receba uma lista de textos. 
# Detecte quais os valores dessa lista são inteiros e em seguida transforme 
# eles para um número do tipo inteiro. Todos esses valores encontrados 
# serão retornados em uma nova lista que deve estar ordenada.

def transforma_lista(lista):
  lista_inteiros = []
  for item in lista:
    if item.isdecimal():
      lista_inteiros.append(int(item))
  lista_inteiros.sort()
  return lista_inteiros

lista = ['12','1213r','6','8','100','3dd']

print(transforma_lista(lista))
