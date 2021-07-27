# Crie uma classe Bola cujos atributos são cor e raio. 
# Crie um método que imprime a cor da bola. 
# Crie um método para calcular a área dessa bola. 
# Crie um método para calcular o volume da bola. 
# Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.

# Obs.:
# Área da esfera = 4*3.14*r*r;
# Volume da esfera = 4*3.14*r*r*r/3

class Bola:
    def __init__(self, cor, raio):
        self.cor = cor     
        self.raio = raio  
    
    def cor_circulo(self):
        return print(f'A cor do cículo é {self.cor}')
    
    def area(self):
        x = 4 * 3.14 * self.raio * self.raio
        return print(f'A área do círculo é de {x}')
    
    def volume(self):
        x = 4 * 3.14 * self.raio * self.raio * self.raio / 3
        return print(f'O volume do círculo é de {x}')
   
circulo = Bola ('Amarelo', 2)
circulo.cor_circulo()
circulo.area()
circulo.volume()
