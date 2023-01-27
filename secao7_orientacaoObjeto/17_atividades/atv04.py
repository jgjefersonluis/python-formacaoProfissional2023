# 4 - Baseado no exercício anterior, cria uma função na classe base que diga 
# a distância percorrida. Vamos supor que esse valor é dado pela peso do veículo
# dividido pela potência do veículo vezes mil. Crie uma moto, carro e um ônibus. 
# Mostre esses valores.

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas
   def distancia_percorrida(self):
     return (self.potencia / self.peso ) * 1000

class Moto(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Carro(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Onibus(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

onibus = Onibus(1000,400, 6)
carro = Carro(300, 100, 4)
moto = Moto(100,50,2)

print("Distancia Percorrida do onibus: ", onibus.distancia_percorrida())
print("Distancia Percorrida do carro: ", carro.distancia_percorrida())
print("Distancia Percorrida da moto: ", moto.distancia_percorrida())
