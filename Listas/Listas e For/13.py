# Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50

from random import randint

lista = []
count = 0
lista_50 = []
while count < 10:
    x = randint(0,100)
    lista.append(x)
    count += 1

for x in lista:
    if x > 50:
        lista_50.append(x)

print(lista)
print(f'Os números sorteados maiores que 50 = {len(lista_50)}')