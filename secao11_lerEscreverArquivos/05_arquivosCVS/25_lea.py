import csv
linhas = [["id","nome", "profissão"],["1","Fernando", "Eng. de Dados"],
          ["2","Maria", "Professora"],["3","Rodrigo", "Dev"]]

with open('pessoas2.csv','w') as file:
  escritorCsv = csv.writer(file)
  escritorCsv.writerows(linhas)
  