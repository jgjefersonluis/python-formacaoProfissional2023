
class Veiculo:
  __numero_veiculos = 0
  def __init__(self,nome, gasolina, potencia):
    self.nome = nome
    self.gasolina = gasolina
    self.potencia = potencia    
    Veiculo.__numero_veiculos += 1
  @staticmethod
  def get_numero_carros():
    return Veiculo.__numero_veiculos

carro =  Veiculo("carro","aditivada",200)
carro2 =  Veiculo("caminhao","aditivada",1000)
print(Veiculo.get_numero_carros())
print(carro.get_numero_carros())

