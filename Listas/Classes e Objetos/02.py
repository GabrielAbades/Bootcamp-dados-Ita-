# Crie uma classe Retângulo cujos atributos são lado_a e lado_b. 
# Crie um método para calcular a área desse retângulo. 
# Crie um objeto dessa classe e calcule a área e a imprima em seguida.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a     
        self.lado_b = lado_b 
    
    def area(self):
        x = self.lado_a * self.lado_b
        return print(f'A área do retângulo é de {x}')

retangulo = Retangulo(10, 20)

retangulo.area()