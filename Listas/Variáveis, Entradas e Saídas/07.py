#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês e depois, calcule e mostre o total do seu salário no referido mês.

x = input('Gostaria de calcular o seu salário mensal agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    sal_hr = float(input('Quanto você ganha por hora?\n'))
    num_hrs = float(input('Quantas horas trabalhou no mês em questão?\n'))

    sal_mes = sal_hr * num_hrs

    print('vALOR DO SALÁRIO EM REAIS:', 'R$' , sal_mes )
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
