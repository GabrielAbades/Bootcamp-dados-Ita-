# Faça uma classe ContaVip que difere da ContaCorrente por ter cheque especial (novo atributo) e 
# é filha da classe ContaCorrente. Você precisa implementar os métodos para saque, transferência ou depósito?

class Cliente():
    def __init__(self, nome='', idade='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade} - Telefone: {self.telefone}'

class ContaCorrente():
    def __init__(self, saldo, cliente=Cliente()):
        self.saldo = saldo
        self.cliente = cliente

    def addCliente(self, nome, idade, telefone):
        self.cliente.append(Cliente(nome, idade, telefone))
    
    def deposito(self):
        choice = 0
        valor_deposito = 0
        if self.saldo > 0:

            while choice != 1:
                nome_titular = input('Qual o nome do titular da conta corrente que vai seu depósito?\n')
                conta_corrente = input(f'Qual o nº da conta corrente de {nome_titular}?\n')
                valor_deposito = int(input('Qual o valor do deposito?\n'))
                print('Confirmacão dos dados:')
                print(f'''
                    Os dados digitados estão corretos?
                    Titular: {nome_titular}
                    Conta Corrente: {conta_corrente}
                    Valor: {valor_deposito}
                    Se estiver correto digite 1 para avançar.
                ''')
            
                choice = int(input(""))

                # Escolhas caso resposta errada
                if choice != 1 :
                    print("Desculpe, não entendi...")
            self.saldo = self.saldo - valor_deposito

            print(f'Seu saldo agora é de R$ {self.saldo}') 
        else:
            print('Saldo insuficiente para realizar o depósito')

    def saque(self):
        if self.saldo > 0:
            valor_saque = int(input(f'Qual o valor pretende sacar? (Saldo: {self.saldo})\n'))
            self.saldo = self.saldo - valor_saque
            print('Saque efetuado com sucesso, retire as notas da boca do caixa')

            print(f'Seu saldo agora é de R$ {self.saldo}') 
        else:
            print('Saldo insuficiente para realizar o saque')
        
    def pix(self):
        choice = 0
        valor_pix = 0
        if self.saldo > 0:
            while choice != 1:
                nome_titular = input('Qual o nome do titular da conta corrente que vai seu depósito?\n')
                chave = input(f'Qual a chave pix do titular {nome_titular}?\n')
                valor_pix = int(input('Qual o valor do pix?\n'))
                print('Confirmacão dos dados:')
                print(f'''
                    Os dados digitados estão corretos?
                    Titular: {nome_titular}
                    Chave Pix: {chave}
                    Valor: {valor_pix}
                    Se estiver correto digite 1 para avançar.
                ''')
            
                choice = int(input(""))

                # Escolhas caso resposta errada
                if choice != 1 :
                    print("Desculpe, não entendi...")
            self.saldo = self.saldo - valor_pix

            print(f'Seu saldo agora é de R$ {self.saldo}') 
        else:
            print('Saldo insuficiente para realizar o pix')

class ContaVip(ContaCorrente):
    def __init__(self, saldo, cheque_especial='', cliente=Cliente()):
        super().__init__(saldo, cliente=Cliente()) 
        self.cheque_especial = cheque_especial

    def addCliente(self, nome, idade, telefone):
        self.cliente.append(Cliente(nome, idade, telefone))
    
    def deposito(self):
        choice = 0
        valor_deposito = 0
        choice2 = 0
        while choice2 != 1 and choice2 != 2:
            print('Confirmacão dos dados:')
            print(f'''
                    1 para utilizar saldo
                    2 para cheque especial
                ''')
            
            choice2 = int(input(""))

                # Escolhas caso resposta errada
            if choice2 != 1 and choice2 != 2 :
                print("Desculpe, não entendi...")
        
            if choice2 == 1:
                if self.saldo > 0:

                    while choice != 1:
                        nome_titular = input('Qual o nome do titular da conta corrente que vai seu depósito?\n')
                        conta_corrente = input(f'Qual o nº da conta corrente de {nome_titular}?\n')
                        valor_deposito = int(input('Qual o valor do deposito?\n'))
                        print('Confirmacão dos dados:')
                        print(f'''
                            Os dados digitados estão corretos?
                            Titular: {nome_titular}
                            Conta Corrente: {conta_corrente}
                            Valor: {valor_deposito}
                            Se estiver correto digite 1 para avançar.
                        ''')
                    
                        choice = int(input(""))

                        # Escolhas caso resposta errada
                        if choice != 1 :
                            print("Desculpe, não entendi...")
                    self.saldo = self.saldo - valor_deposito

                    print(f'Seu saldo agora é de R$ {self.saldo}') 
                else:
                    print('Saldo insuficiente para realizar o depósito')
            if choice2 == 2:
                while choice != 1:
                    nome_titular = input('Qual o nome do titular da conta corrente que vai seu depósito?\n')
                    conta_corrente = input(f'Qual o nº da conta corrente de {nome_titular}?\n')
                    valor_deposito = int(input('Qual o valor do deposito?\n'))
                    print('Confirmacão dos dados:')
                    print(f'''
                            Os dados digitados estão corretos?
                            Titular: {nome_titular}
                            Conta Corrente: {conta_corrente}
                            Valor: {valor_deposito}
                            Se estiver correto digite 1 para avançar.
                        ''')
                    
                    choice = int(input(""))

                        # Escolhas caso resposta errada
                    if choice != 1 :
                        print("Desculpe, não entendi...")

                self.cheque_especial = self.cheque_especial - valor_deposito

                print(f'Seu saldo agora é de R$ {self.cheque_especial}')  

    def saque(self):
        if self.saldo > 0:
            valor_saque = int(input(f'Qual o valor pretende sacar? (Saldo: {self.saldo})\n'))
            self.saldo = self.saldo - valor_saque
            print('Saque efetuado com sucesso, retire as notas da boca do caixa')

            print(f'Seu saldo agora é de R$ {self.saldo}') 
        else:
            print('Saldo insuficiente para realizar o saque')
        
    def pix(self):
        choice = 0
        valor_pix = 0
        if self.saldo > 0:
            while choice != 1:
                nome_titular = input('Qual o nome do titular da conta corrente que vai seu depósito?\n')
                chave = input(f'Qual a chave pix do titular {nome_titular}?\n')
                valor_pix = int(input('Qual o valor do pix?\n'))
                print('Confirmacão dos dados:')
                print(f'''
                    Os dados digitados estão corretos?
                    Titular: {nome_titular}
                    Chave Pix: {chave}
                    Valor: {valor_pix}
                    Se estiver correto digite 1 para avançar.
                ''')
            
                choice = int(input(""))

                # Escolhas caso resposta errada
                if choice != 1 :
                    print("Desculpe, não entendi...")
            self.saldo = self.saldo - valor_pix

            print(f'Seu saldo agora é de R$ {self.saldo}') 
        else:
            print('Saldo insuficiente para realizar o pix')
cliente1 = ContaCorrente(1000, cliente=Cliente('Gabriel', 22, '(11) 98328-5092'))
cliente1 = ContaVip(1000)
cliente1.deposito()
cliente1.saque()
cliente1.pix()