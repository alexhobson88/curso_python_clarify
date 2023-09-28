"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""

# estoque = []

# for cont in range (3):

#     produto = dict(
#         nome = str(input('Nome do Produto: ')),
#         preco = float(input(f'Preço do Produto: '))
#     )
#     estoque.append(produto)

# for produto in estoque:
#     for chave, valor in produto.items():
#         print(f'{chave} | {valor}')
#     print()    


# from datetime import datetime

# def cadastrar_produto():
#     produto = dict(
#         nome_produto = str(input('Nome: ')).title()
#         preco = float(input(' Preço: R$ '))
#         nome_funcionario = str(input('Funcionario: ')).title()
#         dt_cadastro = datetime.now().strfime('%d/%m/%Y | %H:%M')
#     )
#     return produto

# def guardar_estoque(prod):
#     estoque = []
#     estoque.append(prod)




from datetime import datetime
estoque = []

while True:
    menu = int(input('1| Cadastrar\n2| Vizualizar\n3| Sair\n Opção: ' ))
    match menu:
        case 1:  #cadastrando Produto
            produto = dict(
                nome_produto = str(input('Nome: ')).title(),
                preco = float(input(' Preço: R$ ')),
                nome_funcionario = str(input('Funcionario: ')).title(),
                dt_cadastro = datetime.now().strftime('%d/%m/%Y | %H:%M')
            )
            estoque.append(produto)

        case 2: #vizualizar estoque
            for prod in estoque:
                for chave, valor in enumerate(estoque):
                    print(f'(\n Produto{chave+1})')
                    for chave, valor in prod.items():
                        print(f'{chave} → {valor}')
                print()

        case 3:
            break
        case _:
            print('Opção Invalida')
