# 2 - Da mesma forma que o exercício anterior, gere a soma de 100 números 
# aleatórios e mostre o resultado final.

from random import randrange
soma = 0

for i in range(0,100):
  soma += randrange(1,100)

print(soma)
