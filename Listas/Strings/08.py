# Faça uma função que receba um texto e uma palavra, 
# então verifique se a palavra está no texto, retornando True ou False.
import re 

texto = 'O pé do Pedro é pequeno'
palavra = 'pequeno'

resultado = re.search(palavra, texto)
if resultado == None:
    print('False')
else:
    print('True')




