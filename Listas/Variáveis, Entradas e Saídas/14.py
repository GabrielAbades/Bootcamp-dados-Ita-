#Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.

#Use a fórmula matemática:

#y(t) = y(0) + v(0)*t + (g*(t**2)/2)

#Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.


x = input('Gostaria de iniciar agora?'+ '\n * Digite 1 = SIM ou 2 = NÃO *\n')
if x == '1':
    v_inicial = float(input('Digite uma velocidade inicial (em m/s):\n'))
    p_inicial = float(input('Digite uma posição inicial (em m):\n'))
    instante_t = float(input('Digite um instante de tempo (em s):\n'))
    t = float(-10)

    p_final = p_inicial + v_inicial * instante_t + (t*(instante_t**2)/2)
    print('A sua posição final é:', p_final, 'm')
else:
    print('Fechar programa')

print('Obrigado por utilizar nossa solução!')
