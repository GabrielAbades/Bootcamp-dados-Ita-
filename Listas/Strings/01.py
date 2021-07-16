#Faça um programa que peça para o usuário digitar uma palavra e imprima cada letra em uma linha.

import time
s = input('Digite uma palavra:')
for i in range(len(s)):
    time.sleep(0.3)
    print (s[i]) 
