class Segredo:
  def __init__(self):
    self.__segredo = 'Senha123'

  def __printa_segredo(self):
    print(self.__segredo)

  def printa_segredo(self):
    self.__printa_segredo()
  

seg = Segredo()
seg.__printa_segredo()
