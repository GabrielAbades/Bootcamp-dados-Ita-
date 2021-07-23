# Implemente um sistema de busca para o programa do exercício 11. 
# Isto é, se o usuário digitar 4, procure um determinado usuário pelo seu CPF.
nome = str('')
cad = {}


def cadastrar(nome=''):
    # Variáveis
    choice = str(".")
    vitorias = int()
    cabecalho = str("Cadastro de Usuarios")
    cabecalho2 = str("por Gabriel Abades")

    # Página Inicial
    print(10 * "=-")
    print(f"{cabecalho:^20}")
    print(f"{cabecalho2:^20}")
    print(10 * "=-")

    # Escolhas
    while choice not in 'ABCD' or choice == "ABCD":
        print('''
    (A) NOVO CADASTRO
    (B) CADASTRADOS
    (C) PESQUISAR POR CPF
    (D) FECHAR

    ''')
        choice = str(input("")).upper().strip()

        # Escolhas caso resposta errada
        if choice not in ("ABCD") or choice == "ABCD":
            print("Desculpe, não entendi...")
    # Cadastramento
    if choice == "A":
        inserir()

        cadastrar()
    elif choice == "B":
        exibir()

        cadastrar()
    elif choice == "C":
        pesquisar()

        cadastrar()


def exibir():
    for nome in cadastros.keys():
        print("CPF: ", nome, " - Outros dados: ", cadastros[nome])
        

def inserir():
    nome = input('Qual seu nome?')
    idade = input('Qual a sua idade?')
    email = input('Digite seu e-mail:')
    cpf = int(input('Digite seu cpf:'))

    if cadastros.get(nome):
        print("Ja existe cadastrado ",nome)
    else:
        cadastros[cpf] = nome, idade, email, cpf


def pesquisar():
    x = int(input('Digite o cpf para pesquisar:'))
    
    for nome in cadastros.keys():
        if x == nome:
            print("CPF: ", nome, " - Outros dados: ", cadastros[nome])
        else: 
            print('CPF não foi encontrado!')
    
    

cadastros = {}
cadastrar()


