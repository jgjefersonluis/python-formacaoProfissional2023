# 1 - Crie um programa que diga “se você precisar ir ao mercado”. 
# Você precisa ir ao mercado se “faltar comida” ou “se for sábado”. 
# Mostre na saída do programa o valor lógico, indicando sim ou não.

falta_comida = False
e_sabado = True
vou_ao_mercado = falta_comida or e_sabado
print("Preciso ir ao mercado? ", vou_ao_mercado)
