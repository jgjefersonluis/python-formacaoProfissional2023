import csv
class Pessoa:
  def __init__(self, id, nome, profissao):
    self.id = id
    self.nome = nome
    self.profissao = profissao
  
  @staticmethod
  def le_pessoas():
    pessoas = []
    with open('pessoas.csv','r') as arquivo:
      leitor = csv.reader(arquivo, delimiter=',')
      for linha in leitor:
        pessoa = Pessoa(linha[0], linha[1], linha[2])
        pessoas.append(pessoa)
    return pessoas
  
  @staticmethod
  def salva_pessoas(*pessoas):
    with open('pessoas.csv','w') as arquivo:
      escritorCsv = csv.writer(arquivo, delimiter=',')
      for pessoa in pessoas:
        escritorCsv.writerow([pessoa.id,pessoa.nome, pessoa.profissao])

pessoa1 = Pessoa(23,"José","Engenheiro")
pessoa2 = Pessoa(12,"Maria","Arquiteta")
pessoa3 = Pessoa(44,"Ana","Cientista de Dados")

Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3)

lista_pessoa = Pessoa.le_pessoas()

for pessoa in lista_pessoa:
  print(pessoa.id, pessoa.nome, pessoa.profissao)
  