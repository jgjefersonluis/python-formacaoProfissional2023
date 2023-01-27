class Veiculo:
  def __init__(self, marcha):
    self.marcha = marcha
  def aumenta_marcha(self):
    self.marcha +=1
    self.marcha = min(self.marcha,5)
  def diminui_marcha(self):
    self.marcha -= 1
    self.marcha = max(self.marcha,1)

class Palio(Veiculo):
  def __init__(self, marcha):
    Veiculo.__init__(self,marcha)

class EcoSport(Veiculo):
  def __init__(self, marcha):
    Veiculo.__init__(self,marcha)
  def aumenta_marcha(self):
    self.marcha +=1
    self.marcha = min(self.marcha,6)

carro = EcoSport(5)
carro.aumenta_marcha()
print(carro.marcha)
carro.aumenta_marcha()
print(carro.marcha)
