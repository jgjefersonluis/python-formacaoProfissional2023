# 4 - Crie uma lista contendo o nome de todos os meses do ano. 
# Em seguida receba por input o mês (número) em que você nasceu 
# e mostre qual o nome do mês que você nasceu.

meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro')
mes_nascido = int(input("Digite o mês que você nasceu:"))
print("Você nasceu em %s " % (meses[mes_nascido - 1]))
