import datetime
data_txt = input("Digite a data no fomato dia/mês/ano:")
datetime = datetime.datetime.strptime(data_txt,"%d/%m/%Y")
print(datetime)
print(type(datetime))
