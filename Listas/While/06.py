# Faça um programa, usando loops, que peça para um usuário digitar um número
# e que só finaliza quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.

numero = 1
lista = []
while numero > 0:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    numero = numero * 1
else:
    print('Você cancelou a sequencia de números ao digitar 0')

x = sum(lista)
print('A soma dos números digitados é de:', x)


