#APLICANDO MÉTODOS ".is()"
nome = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(nome))
print('Só tem espaços?', nome.isspace())
print('É um número?', nome.isnumeric())
print('É alfabético?', nome.isalpha())
print('É alfanumérico?', nome.isalnum())
print('Está em maiúsculas?', nome.isupper()) #ESTÁ SÓ COM LETRAS MAIÚSCULAS?
print('Está em minúsculas?', nome.islower()) #ESTÁ SÓ COM LETRAS MINÚSCULAS?
print('Está capitalizada?', nome.istitle()) #Palavras iniciam com maiúsculas seguidas de minúsculas?
print('Todos podem ser exibidos na tela?', nome.isprintable()) #TODOS PODEM SER EXIBIDOS NA TELA?