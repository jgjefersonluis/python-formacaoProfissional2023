import xml.etree.ElementTree as xml
import os

no_raiz = xml.Element("DadosPessoais")
no_pessoa = xml.Element("Pessoa", attrib={'Nome':'Rodrigo'})
no_cpf = xml.SubElement(no_pessoa, 'CPF')
no_cpf.text = '123456789'

no_sexo = xml.SubElement(no_pessoa, 'Sexo')
no_sexo.text = 'Masculino'

no_endereco = xml.SubElement(no_pessoa, 'Endereco')
no_endereco.text = 'Rua XYZ'

no_raiz.append(no_pessoa)

arvore = xml.ElementTree(no_raiz)

with open('dados_exemplo.xml','wb') as files:
  arvore.write(files)
  