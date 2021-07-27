# Faça uma função que receba duas listas e retorne o produto item a item dessas listas.

# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].
lista1 = [1, 2, 3]
lista2 = [3, 2, 1]

def soma_listas(lista1, lista2):
    soma = [elemA * elemB for elemA, elemB in zip(lista1, lista2)]

    return soma

print(soma_listas(lista1, lista2))