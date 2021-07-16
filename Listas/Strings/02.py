#Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual,
#copiando letra por letra a palavra digitada, depois imprima a nova string.

import time
s = input('Digite uma palavra:')
for i in range(len(s)):
    time.sleep(0.3)
    print (s[i]) 
x = s
print(x)

