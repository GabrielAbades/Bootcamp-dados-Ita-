# Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3.
# Se o usuário digitar 1, o programa deve cadastrar um novo usuário nos moldes
# do exercício 10 e guardar esse cadastro num dicionário cuja chave será o CPF da pessoa.
# Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; e se o
# usuário digitar 3, o programa deve fechar.

# Exemplo do dicionário:
# ‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ : maria@mail.com}
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
    while choice not in 'ABC' or choice == "ABC":
        print('''
    (A) NOVO CADASTRO
    (B) CADASTRADOS
    (C) FECHAR
    ''')
        choice = str(input("")).upper().strip()

        # Escolhas caso resposta errada
        if choice not in ("ABC") or choice == "ABC":
            print("Desculpe, não entendi...")
    # Cadastramento
    if choice == "A":
        inserir()

        cadastrar()
    elif choice == "B":
        exibir()

        cadastrar()


def exibir():
    for nome in cadastros.keys():
        print("CPF: ", nome, " - Outros dados: ", cadastros[nome])


def inserir():
    nome = input('Qual seu nome?')
    idade = input('Qual a sua idade?')
    email = input('Digite seu e-mail:')
    cpf = input('Digite seu cpf:')

    if cadastros.get(nome):
        print("Ja existe cadastrado ",nome)
    else:
        cadastros[cpf] = nome, idade, email, cpf



cadastros = {}
cadastrar()


# if(__name__ == '__main__'):
#     cadastrar()
