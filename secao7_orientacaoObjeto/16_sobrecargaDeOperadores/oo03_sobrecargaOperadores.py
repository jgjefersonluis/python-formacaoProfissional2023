class MeuNumero:
  def __init__(self,numero):
    self.numero = numero
  def __sub__(self, outro):
    return self.numero - outro.numero

num1 = MeuNumero(20.5)
num2 = MeuNumero(10)

print(num1 - num2)
