# Faça uma função que recebe uma string e retorna ela ao contrário.
# Exemplo: Recebe "teste" e retorna "etset".

palavra = 'teste'

palavra_lista = list(palavra)

palavra_lista.reverse()

print(palavra_lista)

x = ''.join(palavra_lista)

print(x)