"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub). 
"""
class Pessoa:     #Classe Pai
    
    def __init__(self, nome, cpf):
        self._nome = nome   
        self.cpf = cpf

    def getNome(self):
        return self._nome

class Cliente(Pessoa): #Classe Filho
    def __init__(self,nome, cpf, email): #def dentro da classe é metodo, nao funcao
        super().__init__(nome, cpf)   #super chama os dados da classe Pai
        self.email = email

class Funcionario(Pessoa):

    def __init__(self,nome, cpf,matricula):
        Pessoa.__init__(self, nome, cpf)    #da pra usar a clase pai no mesmo padrao, usando o self pra chamar as informacoes
        self.matricula = matricula

    def getNome(self):
        return [self._nome, self.matricula]



funcionario1 = Funcionario('Leo','355','5555')

print(funcionario1.getNome())

