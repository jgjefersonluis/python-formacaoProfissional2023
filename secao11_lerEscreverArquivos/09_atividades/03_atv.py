# 3 - Escreva num arquivo os números de 0 até 100. Uma linha para cada número.

with open('exercicio3.txt','wt') as arquivo:
  for i in range(0,101):
    arquivo.write(str(i) + '\n')
    