# 2 - Cria uma classe que represente uma pessoa. Ela deve possuir um nome, 
# CPF e um dependente, onde o dependente é outra pessoa. 
# Dependente não é obrigatório. Crie duas instâncias: pai e filho, 
# e imprima as saídas.

class Pessoa:
  def __init__(self, nome, cpf, dependente=None):
    self.nome = nome
    self.cpf = cpf
    self.dependente = dependente

filho = Pessoa("Rodrigo","200.300.400-45")
pai = Pessoa("Fernando","100.200.300-34",filho)

print("Nome ", filho.nome, " CPF: ", filho.cpf, " Dependente: " , filho.dependente )
print("Nome ", pai.nome, " CPF: ", pai.cpf, " Dependente: " , pai.dependente.nome )
