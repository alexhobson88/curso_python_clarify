"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""


import time
from datetime import datetime

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Idade: '))
peso = int(input('Peso: '))
alt = float(input('Altura: '))

IMC = (peso / (alt*alt))
print(f'{nome} Seu IMC retornou: {round(IMC,1)}')

if IMC < 18.5:
    print('Abaixo do Peso')
elif IMC >=18.5 and IMC< 24.99:
    print('Peso Normal')

elif IMC>=25.0 and IMC < 29.99:
    print('Excesso de Peso')

elif IMC>=30.0 and IMC < 34.99:
    print('Obesidade Classe I')    

elif IMC>=35.0 and IMC < 39.99:
    print('Obesidade Classe II')

elif IMC>=40:
    print('Obesidade Classe III')

else:
    print('Dado Invalido')
    
print(datetime.now().strftime('%d / %m / %Y'))