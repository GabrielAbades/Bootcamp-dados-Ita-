# Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente. 
# Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.

# Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros. 
# Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente,
# alterar um cadastro ou sair.

dict_clientes = {}
clientes = {}
class Cliente:
    
    def cadastro(clientes=''):
        choice = str(".")
        while choice not in 'ABC' or choice == "ABC":
            print( '*' * 34)
            print('- CADASTRO DE CLIENTES EM PYTHON -')
            print( '*' * 34)
            print('O que deseja fazer agora?')
            print('''
            (A) Novo Cliente
            (B) Alterar Cadastro
            (C) Sair
            ''')
           
            choice = str(input("")).upper().strip()

            # Escolhas caso resposta errada
            if choice not in ("ABC") or choice == "ABC":
                print("Desculpe, não entendi...")
        
        if choice == "A":
            nome = input('Nome do Cliente:\n')
            idade = int(input('idade:\n'))
            telefone = input('Telefone:\n')
            
            dict_clientes[nome] =  idade, telefone
            print(dict_clientes)
            Cliente().cadastro()
        elif choice == "B":
            x = input('Digite o nome do cliente para alterar:\n')
    
            for nome in dict_clientes.keys():
                if x == nome:
                    idade_novo = input('Digite a nova idade:\n')
                    tel_novo = input('Digite o novo telefone:\n')
                    dict_clientes[nome] = idade_novo, tel_novo
                    print(f'''
                    Nome: {nome}
                    Idade: {dict_clientes[nome][0]}
                    Telefone: {dict_clientes[nome][1]}
                    ''')
                   
                else: 
                    print('Contato não foi encontrado!')
            

            Cliente().cadastro()
        else:
            pass
    

               

Cliente().cadastro()





