#Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura em graus Celsius (°C).

#°C = (5 * (F-32) / 9)

#Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a transforme em graus Fahrenheit.

#F to °C
x = input('Conversor de Graus F para °C \n\n'+ 'Gostaria de converter agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    f = float(input('Digite quantos graus pretende converter:\n'))

    c = (5*(f-32)/9)

    print('Graus convertidos:', c , '°C' )
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')

#°C to F
x = input('Conversor de Graus °C para F \n\n'+ 'Gostaria de converter agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    c = float(input('Digite quantos graus pretende converter:\n'))

    f = (c * 9/5)+32

    print('Graus convertidos:', f , 'F' )
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
