import datetime
# y ano
# m mês
# d dia
# H hora formato 00-23
# M minuto
# S segundo

# A dia da semana
# a dia da semana abrev.
# B nome do mês
# b nome do mês abrev.
# I hora formato 12 horas
# p AM PM

data = datetime.datetime(2000,9,30,10,30,20)
print(data.strftime("%A  - %a"))
print(data.strftime("%B  - %b"))
print(data.strftime("%H  - %I"))
print(data.strftime("%I  - %p"))
