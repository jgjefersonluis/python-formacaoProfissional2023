# 5 - Crie um programa que receba como input uma string. 
# Em seguida percorra a string e diga quantos espaços em branco essa string tem.

texto = input("Digite um texto: ")
indice =0
num_vazio =0

while (indice < len(texto)):
  if texto[indice] == " ":
    num_vazio +=1
  indice += 11

print("Número de espaços no texto é de %d " % (num_vazio))
