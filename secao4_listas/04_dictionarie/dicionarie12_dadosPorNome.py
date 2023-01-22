dados_maria = {
    'sexo' : 'feminino',
    'cpf' : '12345678910',
    'rg' : '19487555'
}
dados_joao = {
    'sexo' : 'masculino',
    'cpf' : '12345678745',
    'rg' : '878164'
}
dados_ana = {
    'sexo' : 'feminino',
    'cpf' : '787846555421',
    'rg' : '820000035'
}

dados_por_nome ={
    'ana' : dados_ana,
    'maria': dados_maria,
    'joao' : dados_joao
}

print(dados_por_nome['joao']['sexo'])