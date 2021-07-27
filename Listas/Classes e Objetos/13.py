# Nos exercícios 1, 2, 3, 4 e 6, implemente o método _ repr _ para exibir as 
# informações desejadas de cada uma das classes.

# Exercicio 1
class Bola:
    def __init__(self, cor, raio):
        self.cor = cor     
        self.raio = raio  
    
    def __repr__(self):
        x = 4 * 3.14 * self.raio * self.raio
        y = 4 * 3.14 * self.raio * self.raio * self.raio / 3
        return f'A área do círculo é de {x} | O volume do círculo é de {y}'
  
circulo = Bola ('Amarelo', 2)
print(circulo)


# Exercicio 2 
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a     
        self.lado_b = lado_b 

    def __repr__(self):
        x = self.lado_a * self.lado_b
        return f'A área do retângulo é de {x}'

retangulo = Retangulo(10, 20)

print(retangulo)

# Exercicio 3
class Funcionario:

    def __init__(self, nome, email, mes, horas_trabalhadas, salario_hora):
        self.nome = nome                # atributo 1 
        self.email = email              # atributo 2
        self.mes = mes
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_hora = salario_hora
    
    def __repr__(self):
        x = self.horas_trabalhadas * self.salario_hora
        return f'O salário mensal é de {x}'  

         
funcionario = Funcionario('Gabriel Abades', 'gabrielabades.vlogs@gmail.com', 3, 150, 60)
print(funcionario)

# Exercicio 4 
class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, lista_de_canais, volume):
        self.fabricante = fabricante    
        self.modelo = modelo 
        self.canal_atual = canal_atual 
        self.lista_de_canais = lista_de_canais 
        self.volume = volume 
    def __repr__(self):
    
        return f'''Informações: 
        Fabricante: {self.fabricante} 
        Modelo: {self.modelo}  
        Canal Atual: {self.canal_atual} 
        Lista Canais: {self.lista_de_canais} 
        Volume: {self.volume}''' 
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
print(casa1)

