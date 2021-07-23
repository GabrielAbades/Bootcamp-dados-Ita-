# Faça uma função que receba uma lista e conte quantas vezes
# cada elemento apareceu nessa lista. Essa função deverá
# guardar os dados em um dicionário no qual as chaves são os
# elementos da lista e os valores são a contagem de quantas vezes esse elemento aparece.

lista = [0, 1, 1, 4, 0, 5, 20, 19]
inc = []

def doze(lista):
    inc = []
    dic = {}
    for i in lista:
        num = lista.count(i)
        inc.append(num)
    dict_from_list = dict(zip(lista, inc))

      
    return dict_from_list


print(doze(lista))
