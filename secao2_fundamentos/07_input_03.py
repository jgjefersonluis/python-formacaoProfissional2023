# 2 - Crie um programa que mostre o dia, mês, ano, hora, 
# minuto e segundos inseridos pelo usuário. Formate o valor.

dia = input("Insira o dia: ")
mes = input("Insira o mês: ")
ano = input("Insira o ano: ")
hora = input("Insira a hora: ")
minuto = input("Insira o minuto: ")
segundo = input("Insira o segundo: ")
print("%s/%s/%s %s:%s:%s" % (dia, mes, ano, hora, minuto, segundo))
