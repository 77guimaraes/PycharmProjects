#CONVERTENDO TIPOS

n = input('Digite um numero: ')
#"n" é uma string que está sendo convertida para "float"
print(n)

print(n.isupper()) #ESTÁ SÓ COM LETRAS MAIÚSCULAS?
print(n.isalnum()) #ESTÁ SÓ COM NÚMEROS?
print(n.isalpha()) #ESTÁ SÓ COM ALFABÉTICOS?

nome = str (input('Digite seu nome: '))
print(nome.isupper()) #ESTÁ SÓ COM LETRAS MAIÚSCULAS?
print(nome.isalnum())
print(nome.islower()) #ESTÁ SÓ COM LETRAS MINÚSCULAS?
print(nome.isnumeric())
print(nome.isalpha())
print(nome.isprintable()) #TODOS PODEM SER EXIBIDOS NA TELA?