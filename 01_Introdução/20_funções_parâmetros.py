"""
Parâmetros X Argumentos
"""

def cantar_parabens(nome): #entre parenteses é o parametro
    return f'{nome} Parabens pra voce...'

n = 'Leo'
print (cantar_parabens(n)) #Entre pararentes aqui chama argumento


def soma(num1, num2):
    return num1 + num2

n1 = int(input('Valor para num1: 1'))
n2 = int(input('Valor para num1: 2'))