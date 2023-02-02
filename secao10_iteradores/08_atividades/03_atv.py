# 3 - Crie uma classe iterável chamada “Tabuada” que calcule a tabuada da 
# multiplicação do número recebido no construtor. 
# A cada iteração ela deve retornar um resultado da tabuada. 
# Para testar use um laço for.

class Tabuada:
  def __init__(self, num):
    self.num = num
  def __iter__(self):
    self.atual = 0
    return self
  def __next__(self):
    self.atual += 1
    if(self.atual ==11):
      raise StopIteration
    return self.atual * self.num

tabuada_cal = Tabuada(2)

for i in tabuada_cal:
  print(i)
  