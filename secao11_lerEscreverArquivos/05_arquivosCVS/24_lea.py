import csv
with open("pessoas.csv",'w') as arquivo:
  escritorCsv = csv.writer(arquivo,delimiter=',')
  escritorCsv.writerow(["id","nome", "profissão"])
  escritorCsv.writerow(["1","Fernando", "Eng. de Dados"])
  escritorCsv.writerow(["2","Maria", "Professora"])
  escritorCsv.writerow(["3","Rodrigo", "Dev"])
  escritorCsv.writerow(["4","Irene", "Tec. Informática"])
  