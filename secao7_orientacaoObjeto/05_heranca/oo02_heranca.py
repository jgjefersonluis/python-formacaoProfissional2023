class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  lado = 10

class Triangulo(FormaGeometrica):
  angulo = 30

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

print(quadrado.altura)
print(quadrado.largura)
print(quadrado.lado)

print(triangulo.angulo)
