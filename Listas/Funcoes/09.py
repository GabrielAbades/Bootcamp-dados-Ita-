# Faça uma função que recebe uma lista de palavras e retorna 
# uma lista contendo as mesmas palavras da lista anterior, porém escritas em caixa alta.

lista =  ['gabriel', 'itau', 'letscode']
lista_upper = []
def caixa_alta(lista): 
    for item in lista:
        x = item.upper()
        lista_upper.append(x)


caixa_alta(lista)
print(lista_upper)





