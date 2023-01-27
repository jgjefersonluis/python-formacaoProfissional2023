class Pessoa:
  especie = "Homo Sapiens"
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    print("Pessoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo',34)
pessoa2 = Pessoa("Lucas",21)

print(pessoa1.especie)
print(pessoa2.especie)
