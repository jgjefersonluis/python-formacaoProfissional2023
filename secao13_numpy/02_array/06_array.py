import numpy
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

array = numpy.array([Pessoa("Fernando",45),Pessoa("Rodrigo",23)])
print(array)
print(type(array))
print(array.dtype,  end='\n\n')

print(array[0].nome, array[1].idade)
