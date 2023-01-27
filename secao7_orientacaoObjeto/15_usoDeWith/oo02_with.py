class Lista():
  def __init__(self):
    pass

  def __enter__(self):
    print("Memória Iniciada")
    self.lista = [ i for i in range(0,10)]
    return self.lista

  def __exit__(self, *args, **kwargs):
    print("Memória Liberada")
    del self.lista 

minha_lista = Lista()

with minha_lista as temp_lista:
  for i in temp_lista:
    print(i)

print("Aqui o objeto já não existe mais")
