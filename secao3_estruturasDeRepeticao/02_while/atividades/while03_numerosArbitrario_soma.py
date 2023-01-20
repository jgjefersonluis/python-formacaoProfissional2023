# 3 - Cria um programa que receba um número arbitrário (definido pelo usuário) 
# de números que serão lidos e retorne a soma de todos eles.

numeros_que_devem_ser_lidos = float(input("Digite quantos números serão lidos:"))

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < numeros_que_devem_ser_lidos):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma_atual += num_lido
  numeros_lidos += 1

print("O total é %.2f " % (soma_atual))
