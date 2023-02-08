import re
texto = 'existem 64 predios com 700 metros'
# | => or
info = re.findall('predios|metros', texto)
print(info)
