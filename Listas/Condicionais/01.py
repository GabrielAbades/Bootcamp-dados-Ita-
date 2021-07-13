#Faça um programa que peça a idade da pessoa e imprima se ela é maior ou menor de 18 anos.

x = input('Poderia digitar sua idade agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    idade = int(input('Qual sua idade?'))
    if idade > 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
