import datetime

data_txt = input("Digite a data em que você nasceu em formato dia/mês/ano: ")
data_nascimento = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_agora - data_nascimento
print("Você já vivieu ", diferenca_datas, ' dias')
