# 2 - Crie um programa que faça o calculo do fatorial de um número.
# O fatorial a ser calculado deve ser recebido por input.

fatorial_str = input("Digite o fatorial desejando:")
fatorial_numero = int(fatorial_str)
resultado = 1

for i in range(1, fatorial_numero+1):
  resultado *= i

print("O fatorial de %d é %d " % (fatorial_numero, resultado))
  