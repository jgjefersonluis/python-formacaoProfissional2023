class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  pass

class Triangulo(FormaGeometrica):
  pass

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

print(quadrado.altura)
print(triangulo.largura)
