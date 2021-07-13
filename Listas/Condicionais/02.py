#Faça um programa que peça um número e mostre se ele é positivo ou negativo.

x = input('Poderia digitar um número agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    n = int(input('Digite um número:'))
    if n>=0:
        print ("positivo")
        else:
            print ("negativo")
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
