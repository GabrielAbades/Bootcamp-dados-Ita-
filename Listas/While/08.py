# Faça um programa que peça para o usuário digitar a idade, o salário 
# e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.


#Idade: entre 0 e 150;
idade=int(input("informe a idade--> "))
while ( idade > 150 or idade < 0 ):
	idade=int(input("informe a idade--> "))
	
	
#Salário: maior que zero;
salario=float(input("informe um salário--> "))
while ( salario < 0 ):
	salario=float(input("informe um salário--> "))
	
#Sexo: 'f' ou 'm' ou 'o';

sexo=str(input("informe a inicial do seu sexo--> "))
while sexo !="f" and sexo!="m" and sexo!="o" :
	sexo=str(input("informe a inicial do seu sexo--> "))
	
