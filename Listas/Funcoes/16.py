
# Super Desafio! - Repita o exercício anterior usando recursão, ou seja, 
# uma função que chame ela mesma, lembrando que 3! = 3*2!, que 2! = 2*1!, que 1! = 1*0! e que 0! = 1.
n = int(input('Digite um número para que seu fatorial seja calculado:\n'))

def fatorial(n):
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)
    
print(fatorial(n))
