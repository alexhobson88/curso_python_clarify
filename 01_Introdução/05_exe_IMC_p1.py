"""
Vamos iniciar um programa que receba:
 nome
 idade
 peso
 altura

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Idade: '))
peso = int(input('Peso: '))
alt = float(input('Altura: '))

IMC = (peso / (alt*alt))
print(f'{nome} Seu IMC retornou: {IMC:.2f}')
print(f'{nome} Seu IMC retornou: {round(IMC,2)}')

#peso = int(input'Digite sua idade: ')
#altura = float(input'Digite sua altura: ')






