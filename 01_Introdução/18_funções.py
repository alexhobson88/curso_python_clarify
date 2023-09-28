"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...
"""

# Função diz oi
# Função canta parabéns
# Função soma 2 valores

def diz_oi():
    print('Oi')

diz_oi()

def parabens():
    print('Parabens pra voce\n Nesta data querida')

parabens()


def soma():
    n1 = int(input('Insira primeiro numero: '))
    n2 = int(input('Insira segundo numero: '))
    soma = (n1 + n2)
    print(soma)


def soma2():
    a = 8    
    b = 10
    print(f'Somando {a} com {b}, temos: {a+b}')
soma2()
