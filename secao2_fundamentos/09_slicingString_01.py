"""# Operadores sobre string"""

texto1 = "olá"
texto2 = ", "
texto3 = "tudo bem?"
texto_completo = texto1 + texto2 + texto3
print(texto_completo)

texto1 = "olá"
texto1 += " mundo"
print(texto1)

texto = "Python é bem produtivo,"
texto_repetido = texto * 3
print(texto_repetido)

texto = "exemplo"
print(texto[0])
print(texto[1])

texto = "exemplo"
print(texto[1:4])
print(texto[3:]) #''
print(texto[:5])

texto = "carro"
print(texto[-4])
print(texto[-4:])
print(texto[:-1])
print(texto[-5:-2])

texto = "metro"
print(texto[::-1])
print(texto[3::-1])
print(texto[3:1:-1])

texto = "023"
texto = "1" + texto[1:]
print(texto)

texto = "abcdefg"
texto = texto[:3] + texto[4:]
print(texto)

texto1 = "Olá"
texto2 = "Olá"
igual = texto1 == texto2
print("Textos são iguais? ", igual)

print("a" != "b")

texto = "Programação"
print("a" in texto)
print("e" in texto)
print("Programa" in texto)
print("Programa" not in texto)
print("Vinte" not in texto)

tamanho = len(texto)
print(tamanho)
