# Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
lista1 = [1, 2, 3]
lista2 = [3, 2, 1]

def soma_listas(lista1, lista2):
    soma = [elemA + elemB for elemA, elemB in zip(lista1, lista2)]

    return soma

print(soma_listas(lista1, lista2))