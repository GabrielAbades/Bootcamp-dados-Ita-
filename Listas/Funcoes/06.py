# Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar

numero = int(input('Digite um inteiro: '))

def impar_par(numero):
    if (numero%2) == 0:
        print("Par")
    else:
        print("Ímpar")

impar_par(numero)
