# 2 - Crie uma função que receba uma lista e um número e retorne o elemento 
# da lista na posição deste número. Faça um tratamento para que caso haja um 
# acesso fora do índice a função retorne o valor None.

def acessa_seguro(lista, indice):
  try:
    return lista[indice]
  except:
    return None;

lista = [1]
print(acessa_seguro(lista,0))
