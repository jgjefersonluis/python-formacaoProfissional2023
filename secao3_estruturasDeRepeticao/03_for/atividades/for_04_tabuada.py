# 4 - Cria um programa que printe a tabuada da divisão de um número lido 
# por input.

numero = int(input("Digite a tabuada de divisão desejada: "))
for num in range(1,11):
  print("%d / %d = %f " % (num, numero, num / numero))

