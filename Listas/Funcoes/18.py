#  Desafio 2 - Faça uma função que recebe duas entradas: um input dado pelo
#  usuário e um string que informa o tipo de dado ("idade", "salário" ou "sexo"),
#  e verifica se os dados digitados foram válidos, usando os seguintes critérios:

# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.
def dezoito():
    choice = str(".")
    while choice not in 'ABC' or choice == "ABC":
        print('Selecione um dos itens abaixo para digitar')
        print('''
            (A) IDADE
            (B) SALÁRIO
            (C) SEXO
            ''')
        choice = str(input("")).upper().strip()

        
        if choice not in ("ABC") or choice == "ABC":
            print("Desculpe, não entendi...")


    if choice == "A":
        idade = int(input('Digite sua idade:\n'))
        x = 'IDADE'
        if idade > 0 and idade <= 150 :
            print(f'A {x} DIGITADA É VÁLIDA!')      
        else:
            print(f'A {x} DIGITADA É INVÁLIDA!')
                
            dezoito()

        
    elif choice == "B":
        salario = int(input('Digite seu salario:\n'))
        y = 'SALÁRIO'
        if salario > 0 :
            print(f'O {y} DIGITADO É VÁLIDO!')      
        else:
            print(f'O {y} DIGITADO É INVÁLIDO!')
        dezoito()

    else:
        choice2 = str(".")
        while choice2 not in 'ABC' or choice2 == "ABC":
            print('Selecione um sexo')
            print('''
                (A) MASCULINO
                (B) FEMININO
                (C) OUTRO
                ''')
            choice2 = str(input("")).upper().strip()
            z = 'SEXO'
            
            if choice2 not in ("ABC") or choice2 == "ABC":
                print(f'O {z} DIGITADO É INVÁLIDO!')
                dezoito()
            else:
                print(f'O {z} DIGITADO É VÁLIDO!')
                pass


dezoito()

 


        

