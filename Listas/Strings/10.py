# Desafio - Faça uma função que receba uma string e uma letra e:

# a. imprima quantas vezes a letra aparece na string;

# b. imprima todas as posições em que a letra aparece na string;

# c. retorne a distância entre a primeira e a última aparição dessa letra na string.
string = 'O rato roeu a roupa do rei de roma'.upper()
letra = 'e'.upper()

print('A letra e aparece {} vezes na frase'.format(string.count(letra)))

print('A letra e aparece {} nessa primeira posição na na frase'.format(string.find(letra)))
print('A letra e aparece na ultima posição em {} na frase'.format(string.rfind(letra)))






   