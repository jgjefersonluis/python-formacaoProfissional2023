class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    print("Pessoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo',34)

pessoa1.nome = "Marcelo"
print(pessoa1.nome)
