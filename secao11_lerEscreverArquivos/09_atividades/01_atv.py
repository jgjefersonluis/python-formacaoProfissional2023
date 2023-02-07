# 1 - Leia o seguinte arquivo (“exercicio1.txt”) e transforme em uma lista.

lista = []
with open('exercicio1.txt', 'rt') as arquivo:
  for linha in arquivo:
    lista.append(linha)

print(lista)
