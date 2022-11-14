import re
cena = '35 000'
cena_bp = re.sub(r'\s+', '', cena)

print(cena_bp)