class Pessoa:
  def __init__(self, nome):
    self.__nome = nome

  def get_nome(self):
    print("pegando nome")
    return self.__nome

  nome = property(get_nome) 

instancia = Pessoa("Maria")
print(instancia.nome)
