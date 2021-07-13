# Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
# Dica: Assim como no exercício anterior use três variáveis:
# um contador; 
# uma variável para a soma; 
# e uma variável para os termos. 
# Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.
from math import factorial
from decimal import Decimal
import math
contador = int(0)
soma = int(0)
termo = int(1)
f = int(1)
lista = [] 
while contador < 1000:
    contador += 1
    f = Decimal(math.factorial(contador))
    termo /= f
    lista.append(termo)
 
x = sum(lista)
print("A soma é de:", x)

