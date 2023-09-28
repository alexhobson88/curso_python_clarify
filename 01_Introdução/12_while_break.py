"""
While com Break
while True: >>> este laço será executado enquanto 
não encontrar o Break pelo caminho.
Break >>> Condição de parada de um loop. (FLAG)
"""
# sintaxe
# Validando tipo de dado com break

# qtd_notas = soma_notas = 0

# while True:
#     nota = float(input(f'Digite a {qtd_notas+1}ªnota '))
    
#     if nota >= 0 and nota <= 10:
#         qtd_notas += 1 
#         soma_notas += nota
#     else:
#        print('Nota inválida, Digite Novamente')   

#     if qtd_notas == 4:
#         break    
# # media = soma_notas / qtd_notas
# # print(media)
# # print(f'Média: {round(soma_notas / qtd_notas, 1)}')
# media = round(soma_notas / qtd_notas, 1)
# print(f'Média: {media}')

# if media>=7 and media <= 10:
#     print('\033[42m\nAprovado\033[m')
# elif media >= 5 and media < 7:
#     print('Aluno em Recuperação')
# elif media >= 0 and media < 5:
#     print('\033[31m Reprovado\033[m ')
# else:
#     print('Nota Invalida')


while True:
 menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]SAIR\nOpção: '))

 if menu == 1 or menu == 2:
    n1 = int(input('Valor 1: '))
    n2 = int(input('Valor 2: '))

 match menu:
    case 1: print(f' Resultado da Adição: {n1 + n2}')
    case 2: print(f' Resultado da Subtração: {n1 - n2}')
    case 3: break
    case _: print('Opção Inválida')
    
      