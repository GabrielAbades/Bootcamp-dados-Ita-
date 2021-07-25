# Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.

nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))
nota3 = float(input('Digite a terceira nota:\n'))
nota4 = float(input('Digite a quarta nota:\n'))

lista_notas = [nota1, nota2, nota3, nota4]

x = sum(lista_notas)/ len(lista_notas)

print(f'A média desse aluno é {x}')