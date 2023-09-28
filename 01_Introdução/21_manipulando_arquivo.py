

"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# GITHUB
# STACKOVERFLOW


# with open('./base/teste.txt', 'a', encoding='utf8') as arquivo: # se tiver o 'a' ele vai adicionando outro texto se tiver um w ele vai apagar tudo e inserir um novo
#    arquivo.write('\nTeste, teste, teste')                       # e na latra 'r' é para ler o arquivo
# print(arquivo)

# try:
#  with open('./base/teste.txt', 'r', encoding='utf8') as arquivo:
#   print(arquivo.read())

# except FileExistsError:
#     print('Arquivo nao encontrado')
# except FileNotFoundError:
#     print('Arquivo nao encontrado porque nao existe') 
# finally:
#    print('Volte Sempre')       

# with open('./base/teste.txt', 'w', encoding='utf8') as arquivo:
#    arquivo.write('\nTeste, teste, teste')                       # e na latra 'r' é para ler o arquivo
# print(arquivo)



# import pandas as pd
# dados = pd. read_excel()

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

# Exercício de aula: criar um todo (lista de tarefas)

import encodings


def todo():
    while True:
        try:
            menu = int(input('1| Inserir \n2| Vizualizar \n3| Sair\n'))
        except(ValueError):
            print('Invalido\n')
        
        match menu:
            case 1:
                try:
                    with open('./lista/to-do.txt', 'a', encoding='utf8') as arquivo:
                        while True:
                            tarefa = str(input('Digite uma tarefa ou S para Sair: '))
                            if tarefa.lower() != 's':
                                arquivo.write(f'{tarefa}\n')
                            else:
                                break  
                except(ValueError):
                    print('Invalido')   

            case 2:
                try:
                    with open('./lista/to-do.txt', 'r', encoding='utf8') as arquivo:
                        print(arquivo.read())
                        
                except FileNotFoundError:
                    print('Não Encontrado...')

            case 3:
                break
            case _:
                print('Opção Invalida')
todo()