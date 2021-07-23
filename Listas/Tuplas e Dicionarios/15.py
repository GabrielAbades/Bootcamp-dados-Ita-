# Faça o análogo do exercício 12 para strings: 
# conte quantas vezes cada caracter apareceu nessa 
# string e retorne um dicionário com essa contagem.

lista = ['python', 'itau', 'abades', 'letscode', 'itau', 'python']
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
