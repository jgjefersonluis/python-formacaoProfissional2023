# 2 - Crie  um programa que diga se a senha esta correta e portanto você tem 
# acesso ao sistema. A senha devera ser salva no código, e a tentativa deve ser 
# lida por input.

senha_tentativa = input("Digite a senha: ")
senha_padrao = "1234"
print("Senha está correta? ", senha_tentativa == senha_padrao)
