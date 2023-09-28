"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora


menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\n Opção: '))


if menu >= 1 and menu <5:

    n1 = int(input('Digite numero: '))
    n2 = int(input('Digite numero: '))

    match menu:
        case 1: 
            print('Somando')
            print(n1+n2)
        case 2:
            print('Subtraindo')
            print(n1-n2)
        case 3:
            print('Multiplicar')
            print(n1*n2)
        case 4:
            print('Dividindo')
            print(n1/n2)
        case _:
            print('Opcão Invalida')

else: 
    print('Opcao Invalida')       


''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''

