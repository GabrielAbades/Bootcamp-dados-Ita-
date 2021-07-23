#Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.

# Exemplo:
# Janeiro - 31
# Fevereiro - 28
# Março - 31
# Etc...

dict_ano_mes =[ {
    "Jan": 31,
    "Fev": 28,
    "Mar": 31,
    "Abr": 30,
    "Maio": 31,
    "Jun": 30,
    "Jul": 31,
    "Ago": 30,
    "Set": 31,
    "Out": 30,
    "Nov": 31,
    "Dez": 30
}]
for compra in dict_ano_mes:
    for k, v in compra.items():
        print(k +"-" +str(v))
