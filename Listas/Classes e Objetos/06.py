# O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos. 
# Utilizando essa função, crie uma classe Cronômetro e faça um programa que cronometre o tempo.

import time 
horas = 0
minu = 0
seg = 0
class Cronometro:
    while True:
        time.sleep(1)
        seg += 1
        if seg == 60:
            seg = 0
            minu += 1
        if minu == 60:
            minu = 0
            horas += 1

        if horas < 10:
            if minu < 10:
                if seg < 10:
                    print(f'0{horas}:0{minu}:0{seg}')
                else:
                    print(f'0{horas}:0{minu}:{seg}')
            else:
                if seg < 10:
                    print(f'0{horas}:{minu}:0{seg}')
                else:
                    print(f'0{horas}:{minu}:{seg}')
        else:
            if minu < 10:
                if seg < 10:
                    print(f'{horas}:0{minu}:0{seg}')
                else:
                    print(f'{horas}:0{minu}:{seg}')
            else:
                if seg < 10:
                    print(f'{horas}:{minu}:0{seg}')
                else:
                    print(f'{horas}:{minu}:{seg}')

Cronometro()