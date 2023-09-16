"""
# class => Modelo para os objetos que serão criados
class Aluno:
    # Método construtor __init__
    def __init__(self, mat, nome, curso):
        # Criando atributos
        self.matricula = mat
        self.nome = nome
        self.curso = curso
        self.nota = None

    # Criando um método/função/comportamento
    # Para o Aluno
    def alterarNota(self, nota):
        self.nota = nota
        print("Nota alterada com sucesso!")

    def verificarAprovacao(self):
        if self.nota is None:
            print("O aluno ainda não possui nota!")
            return
        if self.nota >= 6:
            print("O aluno está aprovado!")
        else:
            print("O aluno está de recuperação!")
# Criando um objeto
aluno1 = Aluno(1, "Jonas", "Typescript")
print(f"Nome do aluno: {aluno1.nome}")
aluno1.nome = "Jonas Oliveira"
print(f"Novo nome do aluno: {aluno1.nome}")
aluno1.alterarNota(8.5)
print(f"Nota do aluno: {aluno1.nota}")
aluno1.verificarAprovacao()

aluno2 = Aluno(2, "Mariana", "Django")
aluno2.verificarAprovacao()
"""
""""
# Criando a classe pai/super classe/classe base
class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibirDados(self):
        print("--Dados do Funcionario --")
        print(f'Matricula:{self.matricula}')
        print(f"Nome: {self.nome}")
        print(f"Salario:{self.salario}")


class Gerente(Funcionario):
    pass


class Vendedor(Funcionario):
    def __init__(self, matricula, nome, salario,
                 meta, comissao):
        # Chamando o construtor da superclasse
        super().__init__(matricula, nome, salario)
        self.meta = meta
        self.comissao = comissao
    def exibirDados(self):
        super().exibirDados()
        print(f"Meta do Mês: {self.meta}")
        print(f"Comissão do Mês:{self.comissao}")
class Contador(Funcionario):
    pass

vend1 = Vendedor(1, "Catarina", 3500, 100000, 1500)
print(f"Nome do funcionario: {vend1.nome}")
print(f"Meta do mês: {vend1.meta}")
vend1.exibirDados()
"""

class Conta:
    def __init__(self,conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com Sucesso")
        print(f"Saldo Atual:{self.saldo}")

class Corrente(Conta):
    def __int__(self, conta, nome, saldo, limite_cheque):
        super().__init__(conta, nome, saldo)
        self.limite = limite_cheque
    def sacar(self,valor):
        if valor <= (self.limite + self.saldo):
            self.saldo -= valor
            print(f"Saque Realizado com Sucesso")
            print(f"Seu Saldo Atual:{self.limite}")
        else:
            print("Atingiu o Limite do Cheque Especial")
            print(f"Seu Saldo:{self.limite}")

class Poupanca(Conta):
    def __init__(self,conta, nome, saldo, taxa_rendimento):
        super().__init__(conta, nome, saldo)
        self.taxa = taxa_rendimento

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque Realizado com Sucesso ")
            print(f"Seu Saldo:{self.saldo}")
        else:
            print("Atingiu o limite do Saldo")
            print(f"Seu Saldo:{self.saldo}")
    def calcularRendimento(self):
        self.saldo = self.saldo + self.saldo * self.taxa

cliente1 = Corrente(1, "Alfredo", 2000)
cliente1.sacar(300)