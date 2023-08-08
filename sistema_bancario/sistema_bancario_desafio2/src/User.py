import Account
class User:
    def __init__(*, self,nome: str, data_nascimento: str,cpf: str,endereco: str):
        self.cpf = cpf #unique
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.listAccounts = []
    
    def addAcount(self, account : Account):
        self.listAccounts.append(account)
        