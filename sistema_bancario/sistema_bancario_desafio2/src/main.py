#use cases:
#1 - só deve ser possivel fazer depósitos positivos ( em uma só variavel )
#2 - max 3 saques diarios de no max 500 reais - mensagens de erro
#3 - ter um menu: d / s / e / q  adicional: ajuda
#4 - cadastro de usuario
#5 - cadastro de conta bancária
from DateController import DateController
from Account import Account
from User import User

#variavel usada para ver se o dia mudou
date = DateController.registerMoment()


def userMain(Users):
    global date
    inp = '1'
    while(1):
        checkIfNewDay()
        print(''' Menu de Usuário:\n1 - Entrar\n2 - Criar usuário\n3 - Listar usuários\n4 - Sair\n\n Para navegar bastar digitar a palavra com letra maiúscula ou o numero respctivo''')
        inp = str(input("O que você deseja hoje? "))
        match inp:
            case '1' | 'Entrar':
                findCPF()
            case '2' | 'Criar usuário':
                createUser()
            case '3' | 'Listar usuários':
                UserListAll()
            case '4' | 'Sair:':
                print("Tenha um bom dia!")
                break
            case _:
                print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")

def accountMain(conta :Account):
    global date
    inp = '1'
    while(1):
        checkIfNewDay()
        print(''' Menu:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n Para navegar bastar digitar a palavra com letra maiúscula ou o numero respctivo''')
        inp = str(input("O que você deseja hoje? "))
        match inp:
            case '1' | 'Depósito':
                #Tratamento de caso , para evitar erros
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor <= 0:
                    print("Valor inválido")
                else:
                    SALDO+=float(valor)
                    print(f'Valor depositado {valor},\nSaldo atual R$ {SALDO}')
                    MOVIMENTACAO +=f'Valor depositado {valor},\nSaldo atual R$ {SALDO}\n\n'
            case '2' | 'Saque':
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor >= 0:
                    print("Valor inválido")
            
            case '3' | 'Extrato':
                print(f'\n\n\n\n\n\nMovimentação da conta:\n{MOVIMENTACAO}\n\nSaldo atual: {SALDO:.2f}\n\nLimite: {LIMITE_SAQUE:.2f}\n\n')
                print(f'Valor sacado {valor},\nSaldo atual R$ {SALDO-valor}')
            
            case '4' | 'Sair':
                exit("Tenha um bom dia!")
            
            case _:
                print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")

    
def main():
    #variavel para zerar limite de tranzações no dia (OBS: não estou utilizando nenhum sgbd, caso estivesse seria apenas contar quantas transaçoes e seus respctivos valores para averiguar essa regra de negócio)
    global date
    date = DateController.registerMoment()
    
    Users = list()
    Accounts = list()
    
    
    Users.append(User(cpf="12345678912",
                      nome="Admin",
                      data_nascimento="01/01/2001",
                      endereco="Rua nome,numero,cidade,estado,pais"
                      ))
    Users[0].addAccount(Account(id=len(Accounts),
                                draft_qtd_limit=3,
                                draft_value_limit=500,
                                initial_value_account=0
                                ))
    Users[0].addAccount(Account(id=len(Accounts),
                                draft_qtd_limit=3,
                                draft_value_limit=500,
                                initial_value_account=0
                                ))
    for account in Users[0].listAccount():
        print(account)
    
    



#regras de negócio

def checkIfNewDay():
    global date
    now = DateController.registerMoment()
    if date.day!=now.day:
        date = DateController.registerMoment()
        #update


def createUser():
    pass
def findCPF():
    pass 
def UserListAll():
    pass



















if __name__ == "__main__":
    main()