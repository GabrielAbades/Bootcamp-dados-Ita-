# Desafio 1 - Faça uma função que receba um número e calcule seu fatorial.
import math
numero = int(input('Digite um número para que seu fatorial seja calculado:\n'))
def fact(numero):
    factorial = math.factorial(numero)
    return factorial

print(fact(numero))
