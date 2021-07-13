#Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.
n = int(input("Digite um valor qualquer: "))

i = 1
lista = []
while i <= n:
    lista.append(i)
    i += 1
x = sum(lista)    
print('A soma dos números de 1 a %d eh =' % n, x)
