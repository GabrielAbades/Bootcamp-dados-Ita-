#Faça um programa em que o usuário tem que adivinhar o número escolhido pelo computador. O computador deve sortear um número inteiro de 1 a 5 e pedir para o usuário tentar descobrir qual o número sorteado. Após o usuário digitar sua resposta, o programa deve dizer se ele acertou ou não. Dica: para sortear um número, você precisará utilizar a biblioteca random.

import random

x = random.randint(0, 5)

y = int(input('Digite um número entre 0 e 5 e veja se acertou!\n'))

if x == y:
    print('Parabéns você acertou na mosca!')

else:
    print('Poxa que pena, não foi dessa vez!')
