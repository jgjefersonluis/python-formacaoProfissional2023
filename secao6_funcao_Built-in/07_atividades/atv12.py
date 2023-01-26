# 12 - Leia por input sua próxima data de aniversario no formado Dia/Mês/Ano 
# e mostre quantos dias faltam para seu próximo aniversario.

import datetime
data_txt = input("Digite a data do seu próximo aniversário no formato dia/mes/ano")
data_aniversario = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_aniversario - data_agora
print("Você fará aniversário daqui ", diferenca_datas.days , ' dias')
