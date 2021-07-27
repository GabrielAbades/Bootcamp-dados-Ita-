# Crie uma classe ControleRemoto cujo atributo é televisão 
# (isso é, recebe um objeto da classe do exercício 4). 
# Crie métodos para aumentar/diminuir volume, trocar o canal 
# e sintonizar um novo canal, que adiciona um novo canal à lista 
# de canais (somente se esse canal não estiver nessa lista).

class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante    
        self.modelo = modelo 
        self.canal_atual = canal_atual 
        self.lista_de_canais = lista_de_canais 
        self.volume = volume       

    class controleRemoto:
        def aumentar_diminuir_volume(self):
            vol = int(input('Qual o volume que você deseja?\n'))
            if vol > 0 and vol < 101:
                self.volume = vol
                return print(f'O novo volume é {self.volume}')
            else:
                print('Tente selecionar um valor entre 0 até 100 para continuar...')
        
        def trocar_canal(self):
            canal = input('Qual o canal que você deseja ver agora?\n').upper()
            if canal in self.lista_de_canais:
                self.canal_atual = canal
                return print(f'O novo canal é {self.canal_atual}')
            else:
                self.canal_atual = canal
                self.lista_de_canais.append(canal)
    
                print(f'Novo canal adicionado em sua lista: {self.lista_de_canais}...') 
                
casa1 = Televisor('TCL', 'Smart TV 4K', 'SBT', ['SBT', 'GLOBO', 'SPORTV', 'DISNEY'], 20)  

casa1.controleRemoto().trocar_canal()

    