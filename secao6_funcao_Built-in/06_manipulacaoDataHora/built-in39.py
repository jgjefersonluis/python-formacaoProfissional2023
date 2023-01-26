import datetime

data_2000 = datetime.datetime(2000,1,1,0,0,0)
data_agora = datetime.datetime.now()
diferenca = data_agora - data_2000

print("Desde o ano 2000 passou ", diferenca.days, " dias")
print("Desde o ano 2000 passou ", diferenca.seconds, " segundos")
print("Desde o ano 2000 passou ", diferenca.microseconds, " microsegundos")
                                            
anos = int(diferenca.days/365)
meses = anos * 12

print("Desde o ano 2000 passou ", anos, " anos")
print("Desde o ano 2000 passou ", meses, " meses")

print(diferenca)
