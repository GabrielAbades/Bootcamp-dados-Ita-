#Com a recomendação que as pessoas fiquem em casa e evitem aglomerações como medida pra frear a contaminação pelo coronavírus, como saber quando devemos procurar um hospital? Faça um programa que pergunte os sintomas que a pessoa apresenta e responda se ela deve ou não procurar um hospital.

#Sintomas: a. Você tem febre persistente? b. Você tem dificuldade para respirar?

#A resposta do programa deve seguir a seguinte tabela:

#A	B	Resultado
#Sim	Não	Fique em casa
#Não	Sim	Fique em casa
#Não	Não	Fique em casa
#Sim	Sim	Procure um hospital

print('Verifique seus sintomas (S = SIM e N = NÃO)')
a = input('a. Você tem febre persistente?')
b = input('b. Você tem dificuldade para respirar?')

if a == 'S' and b == 'N':
    print('Fique em casa!')
if a == 'N' and b == 'S':
    print('Fique em casa!')
if a == 'N' and b == 'N':
    print('Fique em casa!')
else:
    print('Procure um hospital!')
