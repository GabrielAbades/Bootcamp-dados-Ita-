#Crie uma tupla com todos os pares entre 0 e 100 (inclusive).

cont = 0
list = []
while cont<100:
    cont = cont + 2
    list.append(cont)


def convert(list):
    return tuple(list)

print(convert(list))