print("Inicio")
lista = [1,2,3]
try: #código que pode dar erro
  print(lista[10])
except: #código executado se der erro
  print("Falha do acessar, linha não encontrada")
else: #código executado se não ser erro
  print("Não houve erro") 
finally: #código executado sempre
  print("Executa sempre")
print("Fim")
