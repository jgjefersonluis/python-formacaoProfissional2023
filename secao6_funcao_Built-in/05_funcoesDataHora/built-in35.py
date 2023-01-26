import datetime
# y ano
# m mês
# d dia
# H hora
# M minuto
# S segundo
atual = datetime.datetime.now()
current_time = atual.strftime("%y/%m/%d %H:%M:%S")
print(current_time)
print(type(current_time))
