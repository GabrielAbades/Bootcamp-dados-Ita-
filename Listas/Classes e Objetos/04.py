# Crie uma classe Televisor cujos atributos são:

# a. fabricante;
# b. modelo;
# c. canal atual;
# d. lista de canais; e
# e. volume.
# Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, 
# que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).
# No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.
# Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um 
# canal que já esteja na lista de canais.

class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante    
        self.modelo = modelo 
        self.canal_atual = canal_atual 
        self.lista_de_canais = lista_de_canais 
        self.volume = volume       

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
            print(f'Sintonize esse novo canal em sua lista...')
    
    def sintonizar(self):
        canal = input('Qual o canal que você deseja sintonizar?\n').upper()
        if canal not in self.lista_de_canais:
            self.canal_atual = canal
            self.lista_de_canais.append(canal)
            print(f'Novo canal adicionado em sua lista: {self.lista_de_canais}...')
        
    

        
casa1 = Televisor('TCL', 'Smart TV 4K', 'SBT', ['SBT', 'GLOBO', 'SPORTV', 'DISNEY'], 20)    
casa1.aumentar_diminuir_volume()
casa1.trocar_canal()
casa1.sintonizar()


 