# 5 - Baseado no exercício anterior, crie os operador '>' e '<' para dizer qual 
# veículo é mais potente. Compare um de cada tipo.
# Observação, sobrescreva os métodos __lt__ e __gt__

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas
   def __lt__(self,outro) :
     return self.potencia < outro.potencia
   def __gt__(self, outro):
     return self.potencia > outro.potencia

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

print(onibus > carro)
print(onibus < moto)
print(moto > carro)
