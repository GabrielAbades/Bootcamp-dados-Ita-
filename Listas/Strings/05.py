#Faça uma função que receba uma string e retorne uma nova string substituindo:
# 'a' por '4'

# 'e' por '3'

# 'I' por '1'

# 't' por '7'

import re

# string de entrada
string = 'Agora isso vai ter que funcionar'

# quebra a string, mas inclui strings vazias
lista = re.split("(\S{1})", string)

# remove strings vazias, deixa apenas o que interessa
final = list(filter(None, lista))

vai = [f.replace('a', '4').replace('e', '3').replace('i', '1').replace('t', '7') for f in final]
x = ' '.join(vai)

print(x)
