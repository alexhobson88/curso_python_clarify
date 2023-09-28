"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.
"""
# tupla1 = ()
# tupla2 = tuple()

# lista1 = []
# lista2 = list()

# n10 = [range(0, 101, 10)]
# n102 = list(range(0, 101, 10))

# print(n102)


# cadastro = []

# cadastro.append('Leo')

# print(cadastro)


# notas = []

# for n in range (4):
#     notas.append(float(input('Nota: ')))


# # notas.sort() #ordenar a lista
# # notas.reverse() #inverte a ordem lista
# print(notas)
# notas.pop(2) #remove ultimo elemento ou pelo indice
# print(notas)
# notas.append(4) #appende insere o dado na lista, nao a posicao
# notas.insert(1,15) #insere dado e posicao na lista
# print(notas)
# notas.remove(7) #remove o pelo item

# print(8 in notas) # se nao existir aparece como falso

notas = [7,4,9,10]
for indice, item in enumerate (notas):
  print(f'Na posição {indice} temos a nota: {item}')