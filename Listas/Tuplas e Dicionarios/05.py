# Faça uma função que recebe valores a, b e c, resolve a equação quadrática a*x**2 + b*x + c = 0 e retorna:
# a. o valor de Δ onde Δ = b**2- 4*a*c
# b. uma tupla com o valor do ponto de mínimo ou máximo: x_m = -b/(2*a) e y_m = -Δ/(4*a);
# c. uma lista contendo as raízes (a lista pode ser vazia, caso Δ<0; pode conter apenas 
# um elemento, caso Δ = 0; ou conter duas raízes, caso Δ> 0).

a = 5
b = 10
c = 3
x_m = -b/(2*a)
y_m = -(100)/(4*a)
print(x_m,y_m  )
def delta(a,b,c):
    delta = (b**2) - (4*a*c)
    x_m = -b/(2*a)
    y_m = -delta/(4*a)
    if delta < 0:
        lista = []
        return {"delta":delta,
            "x_m":[x_m],
            "y_m":[y_m],
            "raizes":lista}
    elif delta == 0:
        lista = []
        x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
        x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
        lista.append(x1)
        lista.append(x2)
        return {"delta":delta,
            "x_m":[x_m],
            "y_m":[y_m],
            "raizes":lista}
    else:
        lista = []
        x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
        x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
        lista.append(x1)
        lista.append(x2)
        return {"delta":delta,
            "x_m":[x_m],
            "y_m":[y_m],
            "raizes":lista}

print(delta(a,b,c))


