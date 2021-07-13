# Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado.
# A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está
# errada e pedir novamente uma resposta ao usuário.
# Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).

import random

x = random.randint(0, 5)
print(x)
y = 1
while y > 0:
    num = int(input('Digite um numero entre 1 e 5 e veja se acertou: '))
    if num == x:
        print('Parabéns você acertou na mosca!')
        y = 0
    else:
        print('Infelizmente a resposta está errada, tente outra vez!!')
        pass





