#use cases:
#1 - só deve ser possivel fazer depósitos positivos ( em uma só variavel )
#2 - max 3 saques diarios de no max 500 reais - mensagens de erro
#3 - ter um menu: d / s / e / q  adicional: ajuda
#4 - cadastro de usuario
#5 - cadastro de conta bancária
from classes.DateController import DateController
from classes.Account import Account
from classes.User import User
from tabulate import *
from src.functions import *

#variavel usada para ver se o dia mudou
date = DateController().registerMoment()


def userMain(Users):
    inp = '1'
    while(1):
        checkIfNewDay(date)
        print(''' Menu de Usuário:\n1 - Entrar\n2 - Criar usuário\n3 - Listar usuários\n4 - Sair\n\n Para navegar bastar digitar a palavra com letra maiúscula ou o numero respctivo''')
        inp = str(input("O que você deseja hoje? "))
        match inp:
            case '1' | 'Entrar':
                SelectedUser  = login(Users)
                if SelectedUser != None:
                    selectAccountMain(SelectedUser)
            case '2' | 'Criar usuário':
                createUser(Users)
            case '3' | 'Listar usuários':
                UserListAll(Users)
            case '4' | 'Sair:':
                print("Tenha um bom dia!")
                break
            case _:
                print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")

def selectAccountMain(user: User):
    global date
    checkIfNewDay(date)
    inp = None
    while(inp!="0"):
        listAccountsToPrint = []
        for account in user.listAccount:
            aux = list()    
            aux.append(account.id)
            aux.append(account.getAccountValue())
            listAccountsToPrint.append(aux)
        print(' Selecione a conta:\n'+tabulate(listAccountsToPrint,headers=["id","saldo"])+"\n-1 - Criar conta"+"\n-2 - Voltar\n")
        inp = int(input("->"))
        if inp == -1:
            createAccount(user)
        if inp==-2:
            return
        for account in user.listAccount:
            if account.id == inp:
                return accountMain(account)
    print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")
    

def accountMain(account :Account):
    global date
    inp = '1'
    while(1):
        checkIfNewDay(date,account=account)
        print(''' Menu:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Voltar\n\n Para navegar bastar digitar a palavra com letra maiúscula ou o numero respctivo''')
        inp = str(input("O que você deseja hoje? "))
        match inp:
            case '1' | 'Depósito':
                #Tratamento de caso , para evitar erros
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor <= 0:
                    print("Valor inválido")
                else:
                    account.moviment(valor)
            case '2' | 'Saque':
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor <= 0:
                    print("Valor inválido")
                else:
                    account.moviment(valor*-1)
                
            case '3' | 'Extrato':
                print(account.showExtract())

            case '4' | 'Voltar':
                break
            case _:
                print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")

    
def main():
    #variavel para zerar limite de tranzações no dia (OBS: não estou utilizando nenhum sgbd, caso estivesse seria apenas contar quantas transaçoes e seus respctivos valores para averiguar essa regra de negócio)
    global date
    date = DateController().registerMoment()
    Users = list()
    userMain(Users)


if __name__ == "__main__":
    main()