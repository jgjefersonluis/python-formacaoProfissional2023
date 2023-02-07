import json
DadosPessoas = {
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
    }
}

texto = json.dumps(DadosPessoas, indent=4)
print(texto)

texto = json.dumps(DadosPessoas, indent=4)
print(texto)

with open('exemplo.json','wt') as arquivo:
  arquivo.write(texto)
  