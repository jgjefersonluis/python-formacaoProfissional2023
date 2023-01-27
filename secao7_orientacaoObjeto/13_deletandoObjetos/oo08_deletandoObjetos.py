class Pessoa:
  def __init__(self, nome):
    self.__nome = nome
  
  @property
  def nome(self):
    return self
  
  @nome.deleter
  def nome(self):
    print("deletando nome")
    del self.__nome

instancia = Pessoa("Larissa")
del instancia.nome
