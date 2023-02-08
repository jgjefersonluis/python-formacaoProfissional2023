import re
texto = 'ABCDefgHI123'
info = re.findall('[A-Z]|[0-9]',texto)
print(info)
