#Como você armazenaria a seguinte tabela usando apenas dicionários? 
# Tente imprimir o valor correspondente da linha Pedro x Coluna B.
#      Coluna A	  Coluna B
# Maria	   1	      5
# Pedro	  0.5	      3
# João	  3.2	      1

notas = [{
    'Maria': (1, 5),
    'Pedro': (0.5, 3),
    'João': (3.2, 1)
}]

for nota in notas:
    count = 0
    for k, v in nota.items():
        count += 1
        if count == 2:
            print('Nome:', k +' '+"|"+ ' ' + 'Coluna B:',str(v[1]))

