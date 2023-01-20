# Operadores de Atribuição e Combinação de Operadores Lógicos

numero = 1 
numero = numero + 1
print(numero)

numero = 1
numero += 1
print(numero)

numero = 10 
numero = numero / 2
print(numero)

numero = 10 
numero /= 2
print(numero)

num = 10
booleana = (num == 10)
print(booleana)

num = 10
booleana = (num != 10)
print(booleana)

num1 = 10
num2 = 20
e_maior = num1 < num2
print(e_maior)

num1 = 21
num2 = 20
e_maior = num1 <= num2
print(e_maior)

num = 11
boolean = num > 0 and num < 10 
print(boolean)

#ver. se é tipo float e igual a 10.1. ou 20.2
num = 10.1
boolean = type(num) == float and (num == 10.1 or num == 20.2)
print(boolean)
