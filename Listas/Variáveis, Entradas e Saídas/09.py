#Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato dd/mm/aaaa.

x = input('Junção de datas para formato dd/mm/yyyy \n\n'+ 'Gostaria de iniciar agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    dia = input('Digite o dia:\n')
    mes = input('Digite o mês:\n')
    ano = input('Digite o ano:\n')

    print('Data seguindo padrão:', dia, '/', mes, '/', ano )
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
