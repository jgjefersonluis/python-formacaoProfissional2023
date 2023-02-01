# 4 - Crie uma classe que represente um caractere (string de tamanho 1), 
# use propriedades ou crie uma função para isso (mas deixe valor privado) e 
# caso o usuário tente inserir um texto gere uma exceção dizendo o motivo.

class Caracter:
  def __init__(self,caracter):
    self.__caracter = ''
    self.caracter = caracter
  
  @property
  def caracter(self):
    return self.__caracter

  @caracter.setter
  def caracter(self, value):
    if len(value)> 1:
      raise Exception("Caracter deve ter no máximo tamanho 1")
    self.__caracter = value

letra = Caracter("a")
print(letra.caracter)

try:
  letra.caracter = 'b'
except Exception as ex:
  print(str(ex))

print(letra.caracter) 
