# Crie uma classe Data cujos atributos são dia, mês e ano. 
# Implemente métodos _ repr _ e para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).

class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def __str__(self):
        if self.dia < 32 and self.mes < 13 and self.ano != 0:
            return f'Data: {self.dia}/{self.mes}/{self.ano}'
        elif self.dia == 24 and self.mes == 10 and self.ano == 2020:
            return f'Data: {self.dia}/{self.mes}/{self.ano} ESSA DATA É DO SEU ANIVERSÁRIO! PARABENS!'
        else:
            return f'Tente novamente, data não corresponde aos padrões solicitados'
    
   

        
tarefa = Data(24, 10, 2020)
print(tarefa)
