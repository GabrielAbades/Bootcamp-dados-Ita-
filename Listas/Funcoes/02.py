# Faça uma função que recebe o valor do raio de um círculo e 
# retorna o valor do comprimento de sua circunferência: C = 2*pi*r.

import math
raio = 10

def circunferencia(raio):
    circu = 2*(math.pi)*raio
    return circu

print(circunferencia(raio))