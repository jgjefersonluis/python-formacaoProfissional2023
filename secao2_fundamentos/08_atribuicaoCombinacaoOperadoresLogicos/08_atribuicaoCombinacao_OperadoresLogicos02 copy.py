# 1 - Crie um programa que responda se você foi aprovado numa prova. 
# Você somente foi aprovado numa prova se sua média for maior ou igual que 7 
# ou se sua nota no exame for maior ou igual a 5. Leia esses valores por input.

media_input = input("Digite sua média nas provas: ")
exame_input = input("Digite sua nota no exame: ")
media_prova = int(media_input)
nota_exame = int(exame_input)
aprovado = (media_prova >=7) or (nota_exame >= 5)
print("Aprovação: ", aprovado)
