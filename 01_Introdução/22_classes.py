"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""

# Criar uma classe cliente   

# class Cliente:

#     def __init__(self,nome, cpf, email): #def dentro da classe é metodo, nao funcao
#         self._nome = nome   #transforma a variavel em privada self.parametro que esta dentro dos parenteses
#         self.cpf = cpf
#         self.email = email

#     def getNome(self):
#         return self._nome

# cliente1 = Cliente('Leo','355','up@uol.com')
# print(cliente1.getNome())

class Funcionario:

    def __init__(self,nome, cpf,matricula):
        self._nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def getNome(self):
        return [self._nome, self.matricula]

funcionario1 = Funcionario('Leo','355','5555')

print(funcionario1.getNome())


# class Funcionario:

#     def __init__(self,nome, cpf, matricula):
#         self._nome = nome
#         self._cpf = cpf
#         self._matricula = matricula

#     def getNome(self):
#         return dict(
#             nome = self._nome,
#             cpf = self._cpf,
#             matricula = self._matricula,       
#         )

# funcionario1 = Funcionario('Leo','355','5555')

# c = funcionario1.getNome
# print(c('cpf'))