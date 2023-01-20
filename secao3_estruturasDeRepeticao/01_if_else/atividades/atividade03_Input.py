# 3 - Crie um programa que fale sobre sua idade. As regras são as seguintes
# você deve receber por input sua idade, se você tiver ate três anos 
# printe que é um bebe, ate 13 anos uma criança, ate 18 anos adolescente, 
# até 65 adulto. Em nenhum deste casos é um idoso

idade = int(input("Digite sua idade: "))
if idade <=3:
  print("Você é um bebe!")
elif idade <= 65:
  print("Você é uma criança!")
elif idade <= 18:
  print("Você é um adolescente!")
elif idade <= 65:
  print("Você é um adulto!")
else:
  print("Você é um idoso!")
  