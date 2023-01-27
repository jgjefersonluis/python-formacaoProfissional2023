class FormaGeometrica:
  def __init__(self, altura, largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  def __init__(self,altura, largura, atributo_quadrado):
    FormaGeometrica.__init__(self, altura, largura)
    self.atributo_quadrado = atributo_quadrado

class Triangulo(FormaGeometrica):
  def __init__(self,altura, largura, atributo_triangulo):
    FormaGeometrica.__init__(self, altura, largura)
    self.atributo_triangulo = atributo_triangulo

quadrado = Quadrado(100,200, 'quadrado')
triangulo = Triangulo(100,200, 'triangulo')

print(quadrado.altura)
print(quadrado.atributo_quadrado)

print(triangulo.largura)
print(triangulo.atributo_triangulo)
