# Faça um programa que dadas duas listas de mesmo tamanho,
#  imprima o produto escalar entre elas.

# OBS: produto escalar é a soma do resultado da multiplicação
# entre o número na posição i da lista1 pelo número na posição
# i da lista2, com i variando de 0 ao tamanho da lista.

def produto_escalar(l1, l2):
    if len(l1) != len(l2):
        return 0
    s = 0.0
    for i in range(len(l1)):
        s = s + l1[i]*l2[i]
    return s

l1 = [1, 2, 3, 4]
l2 = [2, 4, 5, 6]

print(produto_escalar(l1, l2))