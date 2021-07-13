#Escreva um programa que peça a nota de 3 provas de um aluno e mostre se ele passou ou não de ano.

#Obs.: O aluno irá passar de ano se a média das suas notas for maior ou igual a 6 (média é a soma das notas dividido pelo número de provas).

x = input('Poderia digitar um número agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    a = float(input('Digite a primeira nota:'))
    b = float(input('Digite a segunda nota:'))
    c = float(input('Digite a terceira nota:'))
    soma = a + b + c media = soma / 3
    if media >= 6:
        print ('Parabéns sua média foi de:', media)
    else:
        print ('Infelizmente não atingiu o conceito necessário para passar, sua média foi de:', media)
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
