# Crie uma classe Fração cujos atributos são numerador (número de cima) e denominador (número de baixo).

# Implemente os métodos de adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração.
# Implemente também o método _ repr _.
# Implemente métodos para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).
class Fracao():
    x = 0
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.resultado = 0
    def __str__(self):
        return f'Numerador = {self.numerador} | Denominador = {self.denominador}'
    
    def sub(self):
        self.resultado = self.numerador - self.denominador
        return f'Subtração = {self.resultado}'
    
    def som(self):
        self.resultado = self.numerador + self.denominador
        return f'Soma = {self.resultado}'

    def multi(self):
        self.resultado = self.numerador * self.denominador
        return f'Multiplicação = {self.resultado}'
    
    def divi(self):
        self.resultado = self.numerador / self.denominador
        return f'Divisão = {self.resultado}'
        
tarefa = Fracao(10, 5)
print(tarefa)
print(tarefa.sub())
print(tarefa.som())
print(tarefa.multi())
print(tarefa.divi())