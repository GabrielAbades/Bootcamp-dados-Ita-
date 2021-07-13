#Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e). Sabendo a resposta certa, o programa deve receber a opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.

x = input('1) (Univesp-2010) Qual o valor de PI?'+ '\n a) 2.18 \n'+ '\n b) 5.18 \n'+ '\n c) 10 \n'+ '\n d) 3.14 \n')
if x == 'd':
    print ('Parabéns você acertou!')

else:
    print('Errooou, tente novamente!')

print('Obrigado por utilizar nossa solução!')
