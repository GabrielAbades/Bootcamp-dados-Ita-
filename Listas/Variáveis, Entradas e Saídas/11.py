#Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).

#Obs: IMC = Peso/Altura**2


x = input('Gostaria de calcular seu IMC agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    peso = float(input('Digite seu peso:\n'))
    altura = float(input('Digite sua altura:\n'))

    imc = peso/altura**2
    print('Seu IMC é de:', imc )
    if imc <=16.9:
        print('Você esta muito abaixo do peso')
    elif imc >= 17 <=18.4:
        print('Você esta abaixo do peso')
    elif imc >= 18.5 <=24.9:
        print('Você esta no seu peso ideal')
    elif imc >= 25 <=29.9:
        print('Você esta acima do peso')
    elif imc >= 30 <=34.9:
        print('Obesidade grau I')
    elif imc >= 35 <=40:
        print('Procure um médico, obesidade grau II')
    elif imc >=40:
        print('Cuidado você corre sérios riscos, obesidade grau III')
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
