from classes.Account import Account
class User:
    def __init__(self,*,nome: str, data_nascimento: str,cpf: str,endereco: str):
        self.cpf = cpf #unique
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.listAccount = []
    
    def addAccount(self, account : Account):
        self.listAccount.append(account)
    