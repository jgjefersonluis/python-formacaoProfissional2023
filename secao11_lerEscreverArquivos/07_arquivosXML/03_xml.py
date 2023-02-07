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

dados = {
    'Rodrigo' : {
        'CPF': '123456788',
        'Sexo': 'Masculino',
        'Endereco':'Casa 345',
        'Idade': 23
    },
    'Fernando': {
        'CPF': '4545454',
        'Sexo': 'Masculino',
        'Endereco':'Rua y',
        'Idade': 23,
        'Filhos': ["Rodrigo","lucas"]
    },
       'Ana' : {
        'CPF': 'dafdfadf',
        'Sexo': 'Feminino',
        'Endereco':'Casa 345',
        'Idade': 28
    }
}

raiz = xml.Element("DadosPessoais")

for key in dados:
  nome = key
  dados_pessoa = dados[nome]
  cpf = dados_pessoa['CPF']
  sexo = dados_pessoa['Sexo']
  endereco = dados_pessoa['Endereco']
  #idade = dados_pessoa['Idade']
  pessoa = criaTagPessoa(nome, cpf, sexo, endereco)
  if 'Filhos' in dados_pessoa:
    filhos = xml.SubElement(pessoa,'Filhos')
    for filho in dados_pessoa['Filhos']:
      pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
  raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais_3.xml','wb') as files:
  arvore.write(files)
  