#Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:

#a) o produto do dobro do primeiro com metade do segundo.

#b) a soma do triplo do primeiro com o terceiro.

#c) o terceiro elevado ao cubo.


x = input('Gostaria de iniciar agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    z_1 = int(input('Digite o primeiro número inteiro:\n'))
    z_2 = int(input('Digite o segundo número inteiro:\n'))
    r = float(input('Para finalizar, digite um número real:\n'))

    a = z_1 * 2 + z_2 / 2
    b = z_1 * 3 + r
    c = r ** 3

    print('a) o produto do dobro do primeiro com metade do segundo:', a )
    print('b) a soma do triplo do primeiro com o terceiro:', b )
    print('c) o terceiro elevado ao cubo:', c )
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
