"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""

tupla1 = ()
tupla2 = tuple()

lista1 = []
lista2 = list()

dicionario1 = {}
dicionario2 = dict()


paises = {'br : Brasil'}
paises2 = dict(br= 'Brasil')
paises = dict(
    br = 'Brasil',
    py = 'Paraguai',
    ar = 'Argentina'
)
paises['us'] = 'Estados Unidos'  #para adicionar sem alterar os antigos
paises ['br']= Leo    # altera a lista existente sem alterar o Dicionario
paises.update({'us': 'Estados Unidos'}) #mesma coisa do do cima
print(paises)