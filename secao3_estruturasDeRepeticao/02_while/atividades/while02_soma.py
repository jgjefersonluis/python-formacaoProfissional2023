# 2 - Crie um programa que receba 5 números, realiza a soma destes números, 
# mas caso um destes números seja negativo não considere ele na soma.

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  if num_lido >=0:
    soma_atual += num_lido
  numeros_lidos += 1

print("A soma é %.2f " % (soma_atual))
