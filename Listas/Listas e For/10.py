# Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.

# OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.

num1 = input('Digite um número:\n')
num2 = input('Digite um número:\n')
num3 = input('Digite um número:\n')
num4 = input('Digite um número:\n')
num5 = input('Digite um número:\n')

lista = [num1,num1,num3,num4,num5]
lista2 = []
for valor in lista:
    x = float(valor)
    lista2.append(x)


print(lista2)
