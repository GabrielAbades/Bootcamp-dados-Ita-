# Faça uma função que recebe um número x e uma lista numérica e retorna 
# uma lista cujos elementos são os itens da lista de entrada multiplicado por x.

# Exemplo:
# Se a função receber o número 5 e a lista [3,5,1], então a função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].
lista1 = [1, 2, 3]
num = 5
lista_final = []
def multi(lista1, num):
    for i in lista1:
        x = i * num
        final = lista_final.append(x)
    return final
multi(lista1, num)
print(lista_final)