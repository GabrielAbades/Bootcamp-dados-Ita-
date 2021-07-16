#Altere o exercício anterior para que a string copiada alterne entre letras maiúsculas e minúsculas.
#Exemplo: se o usuário digitar "latex" o programa deve imprimir "LaTeX".

import time
s = input('Digite uma palavra:')
for i in range(len(s)):
    time.sleep(0.3)
    print (s[i]) 

s_lista = list(s)
x = len(s_lista) - 1
y = int(x / 2)
z = x - x 

a = s[x].upper()
b = s[y].upper()
c = s[z].upper()

s_lista[x]=a
s_lista[y]=b
s_lista[z]=c


resp = ''.join(s_lista)
print(resp)
