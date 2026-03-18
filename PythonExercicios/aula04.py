#Aula 04 - Primeiros comandos em Python
print('Olá Mundo!')
print(7 + 4) #printa o resultado da soma

#Variáveis
nome = 'Guanabara' #String / str
idade = 25  #inteiro / int
peso = 75.8 #float
print(nome, idade, peso)

#Desafio 1 - Crie um script que receba o nome do usuário
# e print uma mensagem de boas vindas

nome = input ('Qual o seu nome? ')
print ('Bem-vindo', nome, '! Prazer em te conhecer!')

#Desafio 2 - Crie um script que leia o dia, mês e ano de
#nascimento de uma pessoa e mostra uma mensagem com a data formatada
print ('Informe sua data de nasicmento: ')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Vocês nasceu no dia', dia, 'de', mes, 'de', ano)

#Desafio 3 - Crie um script que leia dois numeros e tente mostrar
#a soma entre eles.
print ('Vamos somar números!')
n1 = input ('Digite um número: ')
n2 = input ('Digite outro número: ')
print(n1 + n2)


# idade = input ('Qual a sua idade? ')
# peso = input ('Qual o seu peso? ')
# print(nome)
# print(idade)
# print(peso)

