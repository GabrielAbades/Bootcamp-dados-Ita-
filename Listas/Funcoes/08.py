# Faça uma função que recebe um número n de entrada, 
# sorteia n números aleatórios entre 0 e 100 e retorna a média deles.
from random import randint
num1 = int(input('Digite um número: \n'))
lista =  []
count = 0
while count < num1:
    num = randint(0,100)
    lista.append(num)
    count += 1

def aleatorio(lista):
    media = sum(lista) / len(lista)
    return media
    
print(aleatorio(lista))