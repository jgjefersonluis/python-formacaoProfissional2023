import csv
with open('pessoas.csv','r') as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
    print(linha)
    