# 2 - Crie um programa que responda “se você pode atravessar a rua” 
# na faixa de pedestres. Você pode atravessar a rua se o “sinal estiver  
# vermelho” e “se não houver nenhum carro vindo da direita” E “nem da esquerda”. 
# Altere as variáveis para verificar se o programa esta correto.
# Mostre na saída do programa o valor lógico.

sinal_vermelho = True
carro_vindo_direita = False
carro_vindo_esquerda = False
pode_atravessar = sinal_vermelho and not carro_vindo_direita and not carro_vindo_esquerda
print("Posso atravessar? ", pode_atravessar)
