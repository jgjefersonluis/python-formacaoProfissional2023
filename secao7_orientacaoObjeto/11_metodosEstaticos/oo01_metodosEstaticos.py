
class Veiculo:
  def __init__(self,nome, gasolina, potencia):
    self.nome = nome
    self.gasolina = gasolina
    self.potencia = potencia    
  @classmethod
  def cria_carro(cls):
    return cls('carro','comum',200)
  @classmethod
  def cria_trator(cls):
    return cls('trator','aditivada',500)

veiculo1 = Veiculo.cria_carro()
veiculo2 = Veiculo.cria_trator()

print(veiculo1.nome)
print(veiculo1.gasolina)
print(veiculo1.potencia)
print(veiculo2.nome)
