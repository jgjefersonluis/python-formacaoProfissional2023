# 1 - Crie um programa que receba o seu saldo bancário e o quanto você deve. 
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

saldo_entrada = input("Digite seu saldo: ")
valor_devido_entrada = input("Digite o quanto você deve: ")
saldo = float(saldo_entrada)
devido = float(valor_devido_entrada)
valor_total = saldo - devido
if valor_total >= 0:
  print("Seu saldo é positivo, você tem R$ %.2f" % (valor_total))
else:
  print("Seu saldo é negativo, você deve R$ %.2f" % (valor_total))
  