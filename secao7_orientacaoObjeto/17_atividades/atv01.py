# 1 - Crie uma classe para representar um carro. Ele deve ter um atributo que 
# diga sua potência em cavalos. Outro atributo deve dizer quanto de gasolina 
# por quilômetros ele consome. Cria duas instâncias e mostre os valores.

class Carro:
  def __init__(self, potencia, alcance):
    self.potencia = potencia
    self.alcance = alcance

carro1 = Carro(100,200)
carro2 = Carro(200,350.5)

print("Potência do carro 1: ", carro1.potencia, " cavalos")
print("Alcance do carro 1: ", carro1.alcance, " Km/l")

print("Potência do carro 2: ", carro2.potencia, " cavalos")
print("Alcance do carro 2: ", carro2.alcance, " Km/l")
