#Crie uma tupla com todos os números de 0 a 9. Explore a sintaxe: use e depois não use parênteses.

cont = -1
list = []
while cont<9:
    cont = cont + 1
    list.append(cont)

def convert(list):
    return tuple(list)

print(convert(list))