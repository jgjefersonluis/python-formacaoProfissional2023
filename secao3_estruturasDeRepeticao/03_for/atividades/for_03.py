# 3 - Crie um programa que leia um quantidade arbitraria de textos e 
# concatene eles numa string única.

numero_de_leituras = int(input("Digite o número de textos que serão lidos: "))
texto_total = ""
for i in range(numero_de_leituras):
  texto_total += input("Digite o texto: ")

print("Texto completo: ", texto_total)
