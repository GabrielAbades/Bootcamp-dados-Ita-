# Faça uma função que receba uma string que contém tanto números 
# quanto letras e caracteres especiais, e que separe as letras em 
# uma variável e os números em outra (os caracteres especiais podem ser descartados). 
# Ao final a função deve imprimir as duas variáveis.

string = 'AB@89HGER90!'

letras = []
num = []
for ch in string:
    if ch.isdigit():
        num.append(ch)
    elif ch.isalpha:
        letras.append(ch)
x = ''.join(letras)
y = ''.join(num)
print(x)
print(y)
