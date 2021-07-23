# Crie uma função que receba os valores do nome, 
# idade e e-mail de uma pessoa e guarde-os em um
# dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, 
# respectivamente. Sua função deve retornar esse dicionário.

nome = input('Qual seu nome?')
idade = input('Qual a sua idade?')
email = input('Digite seu e-mail:')

def dados(nome,idade,email):
    dict_dados = {
        'nome': nome,
        'idade': idade,
        'e-mail': email
    }
    return dict_dados

print(dados(nome,idade,email))
