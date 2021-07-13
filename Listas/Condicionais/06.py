#Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

#a. Mora perto da vítima?

#b. Já trabalhou com a vítima?

#c. Telefonou para a vítima?

#d. Esteve no local do crime?

#e. Devia para a vítima?

#Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores abaixo de 1 são liberados.


print('Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não!'+ '\n Responda com S = SIM ou N = NÃO')

a = input('a) Mora perto da vítima?\n')
b = input('b) Já trabalhou com a vítima?\n')
c = input('c) Telefonou para a vítima?\n')
d = input('d) Esteve no local do crime?\n')
e = input('e) Devia para a vítima?\n')
count = 0
if a == 'S':
    count = count + 1
if b == 'S':
    count = count + 1
if c == 'S':
    count = count + 1
if d == 'S':
    count = count + 1
if e == 'S':
    count = count + 1

if count == 5:
    print('Você é o assassino, ta preso mermão')
elif count <= 4 >= 3:
    print('Você é cumplice neh, dançou junto mermão')
elif count == 2:
    print('Ta suspeito isso aqui')
else:
    print('Ta liberado pae')
