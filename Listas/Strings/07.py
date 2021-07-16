# Agora faça uma função que recebe uma palavra e diz se ela é um palíndromo, ou seja, se ela é igual a ela mesma ao contrário.
# Dica: Use a função do exercício 6.

frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
