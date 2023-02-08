import re
texto = 'ABCDefgHI123'

#[]
info1 = re.findall('[Ae3]',texto)
info2 = re.findall('[A-Z]',texto)
info3 = re.findall('[a-z]',texto)
info4 = re.findall('[0-9]',texto)
info5 = re.findall('[A-Za-z]',texto)
print(info1)
print(info2)
print(info3)
print(info4)
print(info5)
