"""
For >>> Utilizada quando se sabe a quantidade de repetições,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe:
for item in iteravel:
    bloco que será executado

* Range -> inicio, fim, passo
* Enumerate -> Permite acesso ao índice
"""

# sintaxe
#indice 
# nome = 'Leonardo'
# # L E O N A R D O
# # 0 1 2 3 4 5 6 7
# #        -3 -2 -1
# print(nome[2:1])
# print(nome[:5]) #Leonardo
# print(nome[2:4]) #on
# print(nome[-1]) #Ultimo indice
# #python conta o zero antes

#for item in iteravel:
#pode usar 
#soma+=num para ter o mesmo efeito do soma = soma + num
#exemplo

# soma = 0
# for contador in range (5):
#     print(soma)
#     num = int(input ('Digite um numero: '))
#     soma += num

# print(soma)

'''
Desafio de aula: Crie um sistema que receba 4 notas 
e calcule a média, ao fim apresente a média e situção
do aluno, sendo:
>7 aprovado, >5 em recuperação e <5 reprovado.
'''
# nota1 = float(input('Digite a 1 media: '))
# nota2 = float(input('Digite a 2 media: '))
# nota3 = float(input('Digite a 3 media: '))
# nota4 = float(input('Digite a 4 media: '))
# media = (nota1+nota2+nota3+nota4)/4

# print(media)

notas = 0
for n in range (4):
    media = float(input (f'Digite a {n+1}º media do aluno: '))
    if n >=0 and n <=10:
     notas = notas + media
    else:
        print('Nota não registrada') 
media = notas / n
print(round(media,2))

if media>=7 and media <= 10:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Aluno em Recuperação')
elif media >= 0 and media < 5:
    print('Reprovado')
else:
    print('Nota Invalida')