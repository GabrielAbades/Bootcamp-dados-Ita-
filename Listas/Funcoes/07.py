# Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.
from random import randint

lista =  []
count = 0
while count < 11:
    num = randint(0,100)
    lista.append(num)
    count += 1

def aleatorio(lista):
    maximo = max(lista)
    print(num)
    
aleatorio(lista)

