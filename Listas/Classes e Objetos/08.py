# Crie uma classe Cliente cujos atributos são nome, idade e e-mail. 
# Construa um método que imprima as informações tal como abaixo:
# Nome: Fulano de Tal
# Idade: 40
# E-mail: fulano@mail.com

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade 
        self.email = email 

    def mostrar(self):
        return print(f'''
            Nome: {self.nome}

            Idade: {self.idade}
            
            E-mail: {self.email}
            ''') 

cliente1 = Cliente('Gabriel', 22, 'gabriel@email.com')    
cliente1.mostrar()