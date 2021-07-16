# Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string:

# Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "

import re

# string de entrada
string = input('Digite uma palavra:')

# quebra a string, mas inclui strings vazias
lista = re.split("(\S{1})", string)

# remove strings vazias, deixa apenas o que interessa
final = list(filter(None, lista))

x = ' '.join(final)

print(final)
print(x)
