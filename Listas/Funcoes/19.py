# Super Desafio! - Refaça o desafio 3 usando recursão.
numero = int(input('Digite um número para calcular sua sequencia de fibonnaci:\n'))
def fibonaci(numero):
  if numero <= 1:
    return numero
  else:
    return fibonaci(numero-1) + fibonaci(numero-2)

print(fibonaci(numero))