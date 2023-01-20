# Formatação

# %s texto
# %d inteiro
# %f real

nome = "Ana"
texto_formatado = "O nome dela é %s " % (nome)
print(texto_formatado)

nome = "Kobe"
idade = 41
altura = 1.98
texto = "Meu nome é %s. tenho %d anos e tenho %f metros de altura" % (nome, idade, altura)
print(texto)

numero_gigante = 1.123456789
print("Número gigante formatado: %.2f" % (numero_gigante))

valor = False
print("O valor é %s" % (valor))
print("O valor é %d" % (valor))

decimal = 23.4566
print("A parte inteira é %d" % (decimal))

texto = "Olá, assim se quebra uma linha,\n\tentendeu como quebra a linha?\n\t\tfim"
print(texto)

texto = 'Deixa a \'palavra\' entre aspas'
print(texto)