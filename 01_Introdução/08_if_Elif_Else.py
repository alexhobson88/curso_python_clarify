"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''
#if 10>40:
 #   print('Ok, é maior')



# nota = 7

# # if nota >= 7:
# #     print('Aluno Aprovado')
# # else: 
# #     print('Aluno Reprovado')    
# nota = float(input('Nota: '))


# if nota>=7 and nota <= 10:
#     print('Aprovado')
# elif nota >= 5 and nota < 7:
#     print('Aluno em Recuperação')
# elif nota >= 0 and nota < 5:
#     print('Reprovado')
# else:
#     print('Nota Invalida')        

# Condição simples
# Condição composta
# Condição aninhada
''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''

idade = int(input('Idade: '))

if idade >= 18 and idade <130:
    print('Apto')
elif idade >= 16 and idade < 18:  
     resp = str(input('Tem autorização? [s  | n]')).lower().strip()

     if resp =='s':
         print('Apto')

     elif resp =='n':
         print('Inapto')
     else:
        print('Resposta Invalida')          

elif idade < 16 and idade > 0:
    print('Inapto')    
else:
    print('Invalido')



# Operadores unitários >>> Dependem de um único valor >>> not, is
num = 10

# Operadores binários >>> Dependem de mais que 1 valor >>> and, or
''