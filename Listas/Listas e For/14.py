# Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

# a. o maior número sorteado;
# b. o menor número sorteado;
# c. a média dos números sorteados;
# d. a soma dos números sorteados.

from random import randint

lista = []
count = 0
lista_50 = []
while count < 10:
    x = randint(0,100)
    lista.append(x)
    count += 1
print(lista)
print(f'a. o maior número sorteado = {max(lista)}')
print(f'b. o menor número sorteado = {min(lista)}')
print(f'c. a média dos números sorteados = {sum(lista)/len(lista)}')
print(f'd. a soma dos números sorteados = {sum(lista)}')