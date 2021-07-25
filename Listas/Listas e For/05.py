# Faça um programa que imprima o maior número de uma lista, sem usar a função max()
def maior_valor(lista):
    
        if len(lista) == 0:
            return None

        maior = lista[0]

        for valor in lista:
            if valor > maior:
                maior = valor

        return maior
 
lista = [1,32,4,7,9,10,22,10]
print(maior_valor(lista))