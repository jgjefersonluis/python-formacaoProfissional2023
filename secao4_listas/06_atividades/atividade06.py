# 6 - Escolha três objetos de sua escolha e em seguida cria uma lista para 
# armazenar o objeto e sua função. Agora por input receba o nome desse objeto 
# e imprima a sua função. Caso o objeto não exista, informa ao usuário.

objetos = {
    'Cadeira' : 'Serve para sentarmos',
    'Monitor' : 'Serve para visualizar o processamento',
    'Mouse'   : 'Serve para realizar operações' 
}
objeto_procurado = input("Digite o objeto: ")
if objeto_procurado in objetos:
  print(objetos[objeto_procurado])
else:
  print("Objeto não encontrado")
  