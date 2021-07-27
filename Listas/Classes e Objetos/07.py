# Crie uma modelagem de classes para uma agenda capaz de armazenar contatos. 
# Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.
dict_contatos = {}
contatos = {}
class Agenda:
    
    def agenda(contatos=''):
        choice = str(".")
        while choice not in 'ABCDE' or choice == "ABCDE":
            print( '*' * 25)
            print('--- AGENDA EM PYTHON ---')
            print( '*' * 25)
            print('O que deseja fazer agora?')
            print('''
            (A) Novo Contato
            (B) Buscar Contatos
            (C) Remover Contato
            (D) Listar Contatos
            (E) Fechar
            ''')
           
            choice = str(input("")).upper().strip()

            # Escolhas caso resposta errada
            if choice not in ("ABCDE") or choice == "ABCDE":
                print("Desculpe, não entendi...")
        
        if choice == "A":
            nome = input('Nome do Contato:\n')
            telefone = input('Telefone:\n')
            email = input('E-mail:\n')
            endereco = input('Endereço:\n')
            
            dict_contatos[nome] =  telefone, email, endereco
            print(dict_contatos)
            Agenda().agenda()
        elif choice == "B":
            x = input('Digite o nome para pesquisar:\n')
    
            for nome in dict_contatos.keys():
                if x == nome:
                    print(f'''
                    Nome: {nome}
                    Telefone: {dict_contatos[nome][0]}
                    E-mail: {dict_contatos[nome][1]}
                    Endereço: {dict_contatos[nome][2]}
                    ''')
                   
                else: 
                    print('Contato não foi encontrado!')
            

            Agenda().agenda()
        elif choice == "C":
            x = input('Digite o nome para remover:\n')
            dict_contatos.pop(x)
            print(dict_contatos)
            Agenda().agenda()
        elif choice == "D":
            print( '*' * 25)
            print('--- LISTA ---')
            print( '*' * 25)

            print(dict_contatos)
            
            Agenda().agenda()
        else:
            pass
    

               

Agenda().agenda()


    


