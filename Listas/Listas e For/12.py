# Sorteie uma lista de 10 números e imprima:

# a. uma lista com os 4 primeiros números;
# b. uma lista com os 5 últimos números;
# c. uma lista contendo apenas os elementos das posições pares;
# d. uma lista contendo apenas os elementos das posições ímpares;
# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
# f. uma lista inversa dos 5 primeiros números;
# g. uma lista inversa dos 5 últimos números.
from random import randint

lista = []
count = 0
while count < 10:
    x = randint(0,100)
    lista.append(x)
    count += 1
    
print(f'Lista gerada randomicamente: {lista}')

lista01 = []
for x in lista[:4]:
    lista01.append(x)
lista02 = []
for x in lista[-5:]:
    lista02.append(x)

impares = list()
pares = list()

for c in lista:
    if c % 2 != 0:
        impares.append(c)
    else:
        pares.append(c)

lista03 = []
for x in lista[::-1]:
    lista03.append(x)

lista04 = []
for x in lista03[:5]:
    lista04.append(x)

lista05 = []
for x in lista03[-5:]:
    lista05.append(x)

print(f'a. uma lista com os 4 primeiros números: {lista01}')
print(f'b. uma lista com os 5 últimos números: {lista02}')
print(f'c. uma lista contendo apenas os elementos das posições pares: {pares}')
print(f'd. uma lista contendo apenas os elementos das posições ímpares: {impares}')
print(f'e. uma lista inversa da lista sorteada: {lista03}')
print(f'f. uma lista inversa dos 5 primeiros números: {lista04}')
print(f'g. uma lista inversa dos 5 últimos números: {lista05}')