# 9 (DESAFIO) - Crie uma lista contendo todos os números de 0 a 100, mas filtre,
# mantendo apenas os números que terminam com 0.

lista = [x for x in range(0,101) if str(x)[-1] == '0']
print(lista)
