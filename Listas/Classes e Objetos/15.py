# Crie uma classe Quadrado, filha da classe Retângulo do exercício 2.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a     
        self.lado_b = lado_b 
    
    def area(self):
        x = self.lado_a * self.lado_b
        return print(f'A área do retângulo é de {x}')
class Quadrado(Retangulo):
    def __init__(self, lado_a, lado_b, lado_a_quadrado, lado_b_quadrado):
        super().__init__(lado_a, lado_b) 
        self.lado_a_quadrado = lado_a_quadrado
        self.lado_b_quadrado = lado_b_quadrado
    
    def area_quadrado(self):
        x = self.lado_a_quadrado * self.lado_b_quadrado
        return print(f'A área do quadrado é de {x}')

retangulo = Retangulo(10, 20)
retangulo = Quadrado(10, 20, 2, 6)
retangulo.area()
retangulo.area_quadrado()
