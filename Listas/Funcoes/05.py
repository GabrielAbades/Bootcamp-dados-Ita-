# Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, 
# caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h 
# e “Boa noite, [nome]” se for após às 18h.

nome = str(input("Digite um nome:"))

hora = float(input("Digite a hora:"))

def horario(nome, hora):
    if hora <= 12:

        print("Bom dia", nome)

    if hora > 12 and hora < 18:

        print("Boa tarde", nome)

    if hora > 18:

        print("Boa noite", nome)

horario(nome, hora)

