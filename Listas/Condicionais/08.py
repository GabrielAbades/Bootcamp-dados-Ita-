#Vamos fazer um radar eletrônico de velocidade. Faça um programa que leia a velocidade de um carro, e diga se ele está acima ou não da velocidade permitida de 50 km/h. Se o carro estiver acima da velocidade, o programa deve imprimir que o motorista ultrapassou a velocidade permitida e recebeu uma multa num determinado valor. Para calcular o valor da multa, considere que para cada quilômetro acima da velocidade permitida, o motorista deve pagar 10 reais.

x = float(input('Digite a velocidade do automovel (em km/h):'))

if x > 50:
    print('Você acaba de receber uma multa')
    multa = x * 10
    print('Valor da multa (em reais):', multa)
else:
    print('Parabens vc anda na lei')
