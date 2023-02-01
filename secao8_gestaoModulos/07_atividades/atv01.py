# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.

from random import randrange
numero = randrange(2,100)
resto = numero % 2
if resto == 0:
  print("O número %d é par" % (numero))
else:
  print("O número %d é impar" % (numero))