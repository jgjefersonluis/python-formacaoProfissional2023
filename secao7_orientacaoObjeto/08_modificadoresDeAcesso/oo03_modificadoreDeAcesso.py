class Base:
  def __base__privada(self):
    print('Pertenco somente a base')
  def _baseprotegida(self):
    print("Pertenco a Base e a quem me herdar")

class Filha(Base):
  def acessa_protegida(self):
    self._baseprotegida()

filha = Filha()
filha.acessa_protegida()
filha._baseprotegida()
