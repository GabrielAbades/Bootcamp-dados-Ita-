# Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1.
# Exemplo: se o usuário digitar 5, o programa deve imprimir [0, 1, 2, 3, 4]

x = int(input('Digite um número:'))
count = 0
lista = []

while(count < x):
    lista.append(count)
    count += 1
    
print(lista)
