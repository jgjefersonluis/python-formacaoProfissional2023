# Casting

texto = "olá"
numero = 2
decimal = 1.5
booleano = True
print(type(texto))
print(type(numero))
print(type(decimal))
print(type(booleano))

texto1 = "2"
texto2 = "1.5"
numero1 = int(texto1)
numero2 = float(texto2)
print(type(texto1))
print(type(numero1))
print(type(numero2))
print(numero1 + numero2)

num = 21.45646
inteira = int(num)
print("A parte inteira de %f é %d" % (num, inteira))

texto = "O número é: "
numero = 10.3
numero_em_string = str(numero)
print(texto, numero_em_string)
print(type(numero_em_string))

numero = 123
texto = str(numero)
numero_de_digitos = len(texto)
print("O número %s tem %d digitos " % (texto, numero_de_digitos))

vazio = None
numero_um = 15
numero_zero = 0
texto = "Texto"
texto_vazio = ""
decimal_zero = 0.0
decimal = 3.5

print("Variável tem valor: ", bool(vazio))

print("Número tem valor: ", bool(numero_um))
print("Número tem valor: ", bool(numero_zero))

print("String tem conteúdo: ", bool(texto))
print("String tem conteúdo: ", bool(texto_vazio))

print("Float tem valor: ", bool(decimal_zero))
print("Float tem valor: ", bool(decimal))
