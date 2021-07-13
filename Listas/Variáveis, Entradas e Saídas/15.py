#Desafio 2 - Faça um programa que informe a data e a hora para o usuário. Para isso use a função datetime.now() do módulo datetime.

import datetime

agora = datetime.now()
formato = "%d/%m/%Y %H:%M:%S" # Definimos um formato 
agora_formatado = datetime.strftime(agora,formato) # Usamos a função strftime(), que formata automaticamente o texto
print(agora_formatado)
