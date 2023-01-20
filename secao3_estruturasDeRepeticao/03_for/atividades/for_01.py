# 1 - Crie um programa que receba uma string por input e conte quantos 
# caracteres ela têm, não leve em conta caracteres de espaço. 
# Você não deve usar o len().

texto = input("Digite um texto:")
num_caracteres = 0

for letra in texto:
  if (letra != " "):
    num_caracteres += 1

print("Tem %d caracteres no texto: " % (num_caracteres))
