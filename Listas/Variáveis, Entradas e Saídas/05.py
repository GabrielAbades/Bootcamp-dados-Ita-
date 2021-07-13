#Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.

#Resposta
x = input('Gostaria de calcular a média do bimestre agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    nota_1 = float(input('Digite a primeira nota:'))
    nota_2 = float(input('Digite a segunda nota:'))
    nota_3 = float(input('Digite a terceira nota:'))
    nota_4 = float(input('Digite a quarta nota:')) s
    oma = nota_1 + nota_2 + nota_3 + nota_4
    media = soma/4

    print('A média bimestral é de:', media)
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
