# 1 - Crie um programa que leia por input dois números e realize
# a divisão entre ambos. Formate o print para mostrar o cálculo completo.

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")
divisao =  float(num1) / float(num2)
print("%s dividido por %s é %.2f" % (num1, num2, divisao) )
