class Teste:
  def __init__(self, num):
    self.num = num

variavel = Teste(10)
print(variavel.num)

del variavel.num

print(variavel.num)
