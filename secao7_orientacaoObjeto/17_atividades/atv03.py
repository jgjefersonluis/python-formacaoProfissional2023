# 3 - Crie uma classe base que represente um veículo. 
# Os atributos devem ser peso do veiculo, número de rodas e potência. 
# Em seguida crie três classes que herdam esse veículo: ônibus, carro e moto. 
# Crie uma instância de cada tipo e imprima as instâncias

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas

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

print("Onibus, Peso: ", onibus.peso, " Potência: ", onibus.potencia, " Rodas ", onibus.rodas)
print("Carro, Peso: ", carro.peso, " Potência: ", carro.potencia, " Rodas ", carro.rodas)
print("Moto, Peso: ", moto.peso, " Potência: ", moto.potencia, " Rodas ", moto.rodas)
