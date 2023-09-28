"""
Python possui o que chamamos de tipagem fraca.

STRING por padrão, sempre estará entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentário.
"""
# Fatiamento de String
# Metodos (podem ser utilizados na mesma construção.)
# Número inteiro - int | ex: 123 65 98 90
# Float >>> Números reais/ decimais separados por . e não ,
# correto
# errado
# Booleano >>> 2 constantes - Verdadeiro (True) e falso (false).


nome = str(input('Digite seu nome: ')).title
dado = 'AleX HoBson    '

print(dado)
print(dado.lower())
print(dado.upper())
print(dado.title())
print(dado.capitalize())

print(len(dado))
print(len(dado.strip()))
print(dado.strip().count(' '))

print(dado.replace('a','10'))

#inteiro (int)
numero = 10
print(numero * 100)

idade = int(input('IDade: '))

#Float
altura = 1.83
alt = float(input('Altura: '))
# Booleando
status = True
status = False
print('a' in 'MAria')
