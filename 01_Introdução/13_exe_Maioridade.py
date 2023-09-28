"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""
from datetime import date
ano_atual = date.today().year
qtd_maior = qtd_menor = soma_menor = 0
for cont in range(5):
    ano_nasc = int(input('Digite Ano de Nascimento: '))

    if(ano_atual - ano_nasc)>= 18:
        qtd_maior += 1
        print('Mais uma pessoa maior de idade\n')
    else:
        qtd_menor += 1
        soma_menor += 18 - (ano_atual - ano_nasc)
        print('Mais uma pessoa menor de idade\n')

media = soma_menor / qtd_menor
print(media)

# qtd_datas = 1
# soma_datas = 0
# while qtd_datas < 6:
#     data = int(input(f'Digite a {qtd_datas}ª data '))
#     idade = 2023 - data
#     qtd_datas += 1 
#     soma_datas += data

# if idade < 18:
#     print('Menor')