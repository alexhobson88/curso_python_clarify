"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""

# repetindo um texto 5 vezes com for
# for cont in range (5):
#     print('Batata')


# repetindo um texto 5 vezes com while

# numero = 0
# while numero < 9:
#     print('Frita')
#     numero += 1

# validando uma senha de forma simples


# senha_cadastrada = str(input('Cadastre uma senha: ')).lower()
# senha = ''

# while senha != senha_cadastrada:
#     senha = str(input('digite sua senha: '))
#     if senha != senha_cadastrada:
#         print('\033[31m Senha incorreta \033[m]')

# print ('\033[42m\nAcesso Permitido\033[m')

qtd_notas = 1
soma_notas = 0
while qtd_notas < 5:
    nota = float(input(f'Digite a {qtd_notas}ªnota '))
    if nota >= 0 and nota <= 10:
        qtd_notas += 1 
        soma_notas += nota
    else:
       print('Nota inválida, Digite Novamente')   
        
# media = soma_notas / qtd_notas
# print(media)
# print(f'Média: {round(soma_notas / qtd_notas, 1)}')
media = round(soma_notas / qtd_notas+1, 1)
print(f'Média: {media}')

if media>=7 and media <= 10:
    print('\033[42m\nAprovado\033[m')
elif media >= 5 and media < 7:
    print('Aluno em Recuperação')
elif media >= 0 and media < 5:
    print('\033[31m Reprovado\033[m ')
else:
    print('Nota Invalida')        