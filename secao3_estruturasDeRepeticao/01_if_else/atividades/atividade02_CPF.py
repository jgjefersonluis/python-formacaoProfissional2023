# 2 - Crie um programa que possui uma variável que guarde seu CPF e que guarde 
# uma senha de sua escolha. Em seguida receba por input uma senha do usuário. 
# Caso a senha recebida seja a correta mostre o CPF, 
# caso não diga que a senha esta incorreta.

senha = "123"
cpf = "123.456.789-10"
senha_usuario = input("Digite a senha: ")
if senha_usuario == senha:
  print("Senha correta, seu CPF é %s" % (cpf))
else:
  print("Sua senha está incorreta!")
  