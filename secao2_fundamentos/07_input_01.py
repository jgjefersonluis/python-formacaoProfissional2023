"""# Input"""

valor_escrito = input()
print(type(valor_escrito))
print(valor_escrito)

meu_nome = input()
print("Eu me chamo %s " % (meu_nome))

dia = input("Insira o dia: ")
mes = input("Insira o mês: ")
ano = input("Insira o ano: ")
print("A data inserida for %s/%s/%s " % (dia, mes, ano))

entrada_usuario = input("Digite 1 para verdadeiro e 0 para falso: ")
valor_inteiro = int(entrada_usuario)
valor_logico = bool(valor_inteiro)
print("Você escolheu: %s " % valor_logico)
print("ou ainda, você escolheu: %i " % (valor_inteiro))
