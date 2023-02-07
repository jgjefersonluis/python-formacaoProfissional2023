import xml.etree.ElementTree as xml
import os

def criaTagPessoa(nome, cpf, sexo, endereco):
  no_pessoa = xml.Element("Pessoa", attrib={'Nome':nome})
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf

  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_sexo.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereco')
  no_endereco.text = endereco

  return no_pessoa

raiz = xml.Element("DadosPessoais")
pessoa1 = criaTagPessoa("Rodrigo","1234545","Masculino","Rua abc")
pessoa2 = criaTagPessoa("Maria","432324","Feminino","Rua 123")
pessoa3 = criaTagPessoa("Ana","565677","Feminino","Rua 456")

raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xml','wb') as files:
  arvore.write(files)
  