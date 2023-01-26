from datetime import datetime, timedelta

data_atual = datetime.now()
datafutura1 = data_atual + timedelta(weeks = 4)
datafutura2 = data_atual + timedelta(days = 30)
datafutura3 = data_atual + timedelta(hours = 12)
datafutura4 = data_atual + timedelta(minutes = 60)

print("Data atual: ", data_atual)
print("Mais 4 semanas: ", datafutura1)
print("Mais 30 dias: ", datafutura2)
print("Mais 12 horas: ", datafutura3)
print("Mais 60 minutos: ", datafutura4)
