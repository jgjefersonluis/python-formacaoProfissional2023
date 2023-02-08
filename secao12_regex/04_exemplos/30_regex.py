import re
# DD/MM/AAAA
# O dia pode variar de 00 a 31
# o mês de 00 a 12
# o ano de 0000 a 9999

texto =  '28/05/1998'

info = re.search("^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$" ,texto)
if info != None:
  print("Data válida")
else:
  print("Data Inválida")
