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
print(json.dumps(DadosPessoas, ensure_ascii=False))
print(json.dumps(23))
print(json.dumps(3.14))
print(json.dumps([1,2,3,4,5]))
print(json.dumps(True))
print(json.dumps(None))
