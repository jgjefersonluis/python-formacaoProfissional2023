# 4 - Crie um programa que receba dois números, e também receba do usuário 
# a operação que deve ser feita, as possibilidades são soma(+), subtração (-), 
# divisão(/) e multiplicação(*). 
# Realize a operação escolhida sobre os dois números.

nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o primeiro segundo: "))
operacao = input("Digite a operação: ")

if (operacao == "+"):
  soma = nume1 + nume2
  print("A soma é: ", soma)
elif (operacao == "-"):
  subtracao = nume1 - nume2
  print("A subtração é ", subtracao)
elif (operacao == "*"):
  multiplicacao = nume1 * nume2
  print("A multiplição é ", multiplicacao)
elif (operacao == "/"):
  divisao = nume1 / nume2
  print("A divisão é ", divisao)
else:
  print("Operação Inválida!")
  