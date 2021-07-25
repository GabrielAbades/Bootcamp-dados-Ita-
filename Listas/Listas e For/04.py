# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

valores = [1,32,4,7,9,10,22,10]
impares = list()
pares = list()

for c in valores:
    if c % 2 != 0:
        impares.append(c)
    else:
        pares.append(c)
x = len(pares)
y = len(impares)
print(f'Os números pares são: {pares}, totalizando {x} pares ao todo')
print(f'Os números ímpares são: {impares}, totalizando {y} pares ao todo')

 