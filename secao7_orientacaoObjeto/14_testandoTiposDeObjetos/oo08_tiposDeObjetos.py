class Veiculo:
  def __init__(self):
    pass
  def acelera(self):
    pass

class Moto(Veiculo):
  def __init__(self):
    pass

class Carro(Veiculo):
  def __init__(self):
    pass
  def re(self):
    print("Dando ré")

def faz_re(var):
  if isinstance(var, Carro):
    var.re()
  else:
    print("não tem ré")

motinho = Moto()
carrinho = Carro()

faz_re(motinho)
faz_re(carrinho)
