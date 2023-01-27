
class Natural:
  def __init__(self,numero):
    self.__numero = numero 
  @property
  def numero(self):
    print("pegando numero")
    return self.__numero
  @numero.setter
  def numero(self, value):
    if value >=0:
      self.__numero = value
      print('setando numero para ', value)

numero = Natural(10)
numero.numero = -10
print(numero.numero)
