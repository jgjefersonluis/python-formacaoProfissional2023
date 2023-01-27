class Pessoa:
  def __init__(self, nome):
    self.__nome = nome
  
  def set_nome(self,nome):
    if len(nome)> 0:
      print("Setando nome") 
      self.__nome = nome

  nome = property(fset = set_nome) 

instancia = Pessoa("Maria")
instancia.nome = "Marcos"
#fset, fget, fdel
