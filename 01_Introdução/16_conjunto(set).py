# Sets (conjuntos)
#para adicionar item comando .add
#para adicionar item comando .pop



# tupla1 = ()           #indice e item
# tupla2 = tuple()

# lista1 = []
# lista2 list()

# dicionario = {}       
# dicionario2 = dict()      #chave e valor aceita valor repetido

# Conjunto1 = {'Leo, 10, 10.4, True'}            #indice orde na e retira valores repetidos
# Conjunto2 = set()


# numeros = {9,2,4,5,6,7,4,3,2,}
# numeros.add(200)
# numeros.pop() #so tira a primeira posicao
# numeros.discard(4) #remove o item exato com mesmo nome
# numeros.remove(3) #remove o item exato com mesmo nome, mas se nao existir vai dar erro e travar e sistema
# print(numeros)


# Analise cidades (cada pessoa que entrou colocou a cidade de nascimento)
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina',
          'Salvador','Juiz de Fora', 'Rio de Janeiro', 'Petrolina',
          'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',  'Juiz de Fora',
          'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador',
          'Juiz de Fora',  'Petrolina', 'Salvador', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'São Paulo',
          'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro',
          'Rio de Janeiro', 'Rio de Janeiro',  'São Paulo', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo']

# # Total de Pessoas
# print(f' Total de pessoas: {len(cidade)}')

# # Quantas pessoas são do Rio de Janeiro
# print(f'Total de poessoas do RJ: {cidade.count("Rio de Janeiro")}')

# print(f'Total de pessoas Petrolina: {cidade.count("Petrolina")}')
# print(f'Quantidade de cidades: {len(set(cidade))}')
# print(f'Cidades: {set(cidade)}')


curso_python ={'Leo', 'Juca', 'Maria', 'ALex', 'Ana', 'Beto'}
curso_sql = {'Leo', 'Juca', 'ALex', 'Ana', 'Claudia', 'Roberta', 'Cris'}

total_alunos1 = curso_python.union(curso_sql)
total_alunos2 = curso_python | curso_sql

#Alunos matriculados nos 2 cursos
Ambos_curso1 = curso_python.intersection(curso_sql)
ambos_curso2 = curso_python & curso_sql

#Alunos que estão apenas em um curso
so_python = curso_python.difference(curso_sql)
so_sql = curso_sql.difference(curso_python)

print(f'Qtd AlunosPy:........... {len(curso_python)}')
print(f'Qtd Alunos SQL:......... {len(curso_sql)}')  
print(f'Quantidade total ALunos: {len(total_alunos1)}')
print(f'Alunos em ambos Cursos:. {(Ambos_curso1)}')
print(f'So SQL:................. {len(so_sql)}')
print(f'So Python:.............. {len(so_python)}')