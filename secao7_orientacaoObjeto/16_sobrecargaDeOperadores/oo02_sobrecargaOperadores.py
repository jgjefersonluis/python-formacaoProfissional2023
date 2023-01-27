class MeuNumero:
  def __init__(self,numero):
    self.numero = numero
  def __add__(self, outro):
    soma = self.numero + outro.numero
    return MeuNumero(soma)

num1 = MeuNumero(10)
num2 = MeuNumero(20.5)
num3 = num1 + num2
print(num3.numero)
