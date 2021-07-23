# Crie uma função que recebe uma lista e retorna True 
# se todos os seus elementos forem numéricos (int, float 
# ou string contendo um int ou float) ou False do contrário. 
# A função deve também retornar a lista tratada: transformar
# todas as entradas não numéricas em numéricas ou, no melhor 
# caso, devolver a lista apenas.

lista = [0,2,5,8,20,40]

def verificar_numeros(lista):
    numeros = []
    is_all_number = True 
    
    for elemento in lista:
        if (type(elemento) == int or type(elemento) == float or type(elemento) == str):
            try:
                numero = float(elemento)
                numeros.append(numero)
            except:
                is_all_number = False
        else:
            is_all_number = False
                
    return is_all_number, numeros

print(verificar_numeros(lista))