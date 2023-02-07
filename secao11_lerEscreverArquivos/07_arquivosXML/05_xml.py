import xml.etree.ElementTree as xml
import os

class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia
  
  @staticmethod
  def salva_carros(*carros):
    raiz = xml.Element("Raiz")

    for carro in carros:
      no_carro = xml.Element('Carro')
      no_nome = xml.SubElement(no_carro, 'Nome')
      no_nome.text = carro.nome

      no_potencia = xml.SubElement(no_carro, 'Potencia')
      no_potencia.text = str(carro.potencia)

      raiz.append(no_carro)
    arvore = xml.ElementTree(raiz)
    with open('carros_exemplo.xml','wb') as files:
      arvore.write(files)

  @staticmethod
  def le_carros():
    lista =[]
    tree = xml.parse('carros_exemplo.xml')
    root = tree.getroot()
    for carro in root:
      nome = None
      potencia = None

      for dado in carro:
        if (dado.tag == 'Nome'):
          nome = dado.text
        if (dado.tag == 'Potencia'):
          potencia = dado.text
      carro = Carro(nome, potencia)
      lista.append(carro)
    return lista

carro1 = Carro('Maverik',330)
carro2 = Carro('Nivus',200)
carro3 = Carro('Monza',180)

Carro.salva_carros(carro1,carro2,carro3)

lista_carros = Carro.le_carros()

for carro in lista_carros:
  print(carro.nome, carro.potencia)