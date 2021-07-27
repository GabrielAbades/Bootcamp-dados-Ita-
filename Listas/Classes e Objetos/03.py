# Crie uma classe Funcionario cujos atributos são nome e e-mail. 
# Guarde as horas trabalhadas em um dicionário cujas chaves são o 
# mês em questão e, em outro dicionário, guarde o salário por hora relativo ao mês em questão. 
# Crie um método que retorna o salário mensal do funcionário.

class Funcionario:

    def __init__(self, nome, email, mes, horas_trabalhadas, salario_hora):
        self.nome = nome                # atributo 1 
        self.email = email              # atributo 2
        self.mes = mes
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_hora = salario_hora
        
    def salario_mensal(self, mes):
        return self.horas_trabalhadas * self.salario_hora

         
funcionario = Funcionario('Gabriel Abades', 'gabrielabades.vlogs@gmail.com', 3, 150, 60)

print(funcionario.salario_mensal(3))