#Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
#Obs: Fórmula da área de um círculo: A = 3,14*(r**2), onde r é o raio.

x = input('Gostaria de calcular o raio de um círculo agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    raio = float(input('Digite o raio (em metros):'))
    area = 3.14 * (raio**2)
    print('A área total do círculo é de:', area , 'm')
    
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
