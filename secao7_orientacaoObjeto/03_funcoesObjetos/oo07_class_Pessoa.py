class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
  def print_nome(self):
    print("Meu nome é %s " % (self.nome))

pessoa1 = Pessoa("Rodrigo","34")
pessoa2 = Pessoa("Maria","22")

pessoa1.print_nome()
pessoa2.print_nome()
