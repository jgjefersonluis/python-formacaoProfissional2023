class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura
  def funcao_herdada(self):
    print("Sou herdado")

class Quadrado(FormaGeometrica):
  pass

class Triangulo(FormaGeometrica):
  pass

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

quadrado.funcao_herdada()
triangulo.funcao_herdada()
