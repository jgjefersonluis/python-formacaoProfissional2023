class Pessoa:
  especie = "Homo Sapiens"
  num_pessoas = 0
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    Pessoa.num_pessoas += 1

pessoa1 = Pessoa('Rodrigo',34)
print(Pessoa.num_pessoas)
pessoa2 = Pessoa("Lucas",21)
print(Pessoa.num_pessoas)
pessoa3 = Pessoa("Maria",22)
print(Pessoa.num_pessoas)
