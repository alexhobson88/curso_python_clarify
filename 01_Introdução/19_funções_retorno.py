# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa


# def diz_oi():
#     return 'Oi'

# diz_oi()

# def parabens():
#     return('Parabens pra voce\n Nesta data querida')

# parabens()


# def soma2():
#     n1 = int(input('Insira primeiro numero: '))
#     n2 = int(input('Insira segundo numero: '))
#     soma = (n1 + n2)
#     print(soma2)


# def soma():
#     a = 8     
#     b = 10
#     return a + b     #apos encontrar o return na funcao, a funcao retorna pra cima e nao execurta mais nada nas linhas de baixo
# print(soma() *10)


# Desafio de aula: Cara ou Coroa

from random import random, randint

# print(random())   #Sempre entre 0 e 1
# print(randint(1, 10))    #sempre entre 1 e 10

# def teste():
#     dado = 1

#     if dado >= 5
#         return "é maior que 5"
#     return 'é menor'

def cara_coroa():
    if random() >= 0.5:
        return 'Cara'
    return 'Coroa'

print(cara_coroa())