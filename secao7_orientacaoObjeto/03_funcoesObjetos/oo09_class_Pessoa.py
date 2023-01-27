class Pessoa:
  def __init__(self, nome):
    self.nome = nome
  def insere_idade(self,idade):
    self.idade = idade

rodrigo = Pessoa("Rodrigo")
rodrigo.insere_idade(34)

print(rodrigo.idade)
