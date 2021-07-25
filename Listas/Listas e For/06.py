# Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

# Dica: Use o método próprio de listas .remove().
maximos = []
def maior_valor(lista):
    
        if len(lista) == 0:
            return None
        
        else:
            count = 0 
            while count < 3:
                maximo = max(lista)
                maximos.append(maximo)
                rem = lista.remove(maximo) 
                count += 1

            return maximo, lista


lista = [1,32,4,7,9,10,22,10]
maior_valor(lista)
print(maximos)