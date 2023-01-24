# 10 - Cria uma função recursiva que itere os números de 0 até 10 e printe o 
# resultado de sua divisão inteira com o número três.

def printa_div_3(num):
  if num ==11:
    return
  print(num // 3)
  printa_div_3(num+1)

printa_div_3(0)
