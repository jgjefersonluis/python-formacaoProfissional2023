class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura
  def calcula_area(self):
    pass

class Quadrado(FormaGeometrica):
  def calcula_area(self):
    return self.altura * self.largura

class Triangulo(FormaGeometrica):
  def calcula_area(self):
    return (self.altura * self.largura)/2

quadrado = Quadrado(200,200)
triangulo = Triangulo(200,200)

print(quadrado.calcula_area())
print(triangulo.calcula_area())
