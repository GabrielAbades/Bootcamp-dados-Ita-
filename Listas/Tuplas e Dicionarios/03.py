# Crie uma função que recebe uma lista de números e devolve, nesta ordem, 
# o mínimo, a média, o desvio padrão e o máximo.

# Dica: Use a biblioteca statistics (import statistics) para calcular
# o desvio padrão: desvio = statistics.stdev(lista)
import statistics

list = [0,2,5,8,20,40]

def media_list(list):
    min= statistics.median_low(list)
    media = statistics.mean(list)
    desvio = statistics.stdev(list)
    max = statistics.median_high(list)
    return min, media, desvio, max

print(media_list(list))