# 4 - Percorra os números de 2 até 10 e diga se o número é par ou impar.

num_atual =2
while (num_atual <= 10):
  resto = num_atual % 2
  if (resto ==0):
    print("O número %d é par" % (num_atual))
  else:
    print("O número %d é impar" % (num_atual))
  num_atual +=1
  