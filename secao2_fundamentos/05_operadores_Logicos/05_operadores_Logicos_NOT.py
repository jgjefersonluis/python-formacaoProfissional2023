# 3 - Agora faça a mesma coisa que o exercício anterior, mas desta vez você 
# esta com pressa e para atravessar a rua basta que o sinal esteja vermelho 
# "OU" que não venha carro da esquerda e direita. Altere as variáveis 
# para verificar a resposta em comparação com ao exercício anterior. 
# Mostre na saída do programa o valor lógico.

sinal_vermelho = False
carro_vindo_direita = True
carro_vindo_esquerda = True
pode_atravessar = sinal_vermelho or not carro_vindo_direita and not carro_vindo_esquerda
print("Posso atravessar? ", pode_atravessar)
