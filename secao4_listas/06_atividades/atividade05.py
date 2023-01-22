# 5 - Crie uma lista contendo todos dias (número) do mês em que você nasceu. 
# Em seguida receba por input o dia (número) em que você nasceu e remova 
# desta lista. Ao final mostre o conteúdo da lista.

dias  = []
for i in range(1,32):
  dias.append(i)
dia_nascido = int(input("Digite o número do dia em que você nasceu: "))
dias.remove(dia_nascido)
print(dias)
