#use cases:
#1 - só deve ser possivel fazer depósitos positivos ( em uma só variavel )
#2 - max 3 saques diarios de no max 500 reais - mensagens de erro
#3 - ter um menu: d / s / e / q  adicional: ajuda
#4 - cadastro de usuario
#5 - cadastro de conta bancária
import requests
from classes.DateController import DateController
from classes.Account import Account
from classes.User import User
from tabulate import *

#variavel usada para ver se o dia mudou
date = DateController().registerMoment()


def userMain(Users):
    inp = '1'
    while(1):
        checkIfNewDay()
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
    checkIfNewDay()
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
    inp = '1'
    while(1):
        checkIfNewDay(account=account)
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
    
    
    Users.append(User(cpf="12345678912",
                      nome="Admin",
                      data_nascimento="01/01/2001",
                      endereco=get_cep_request()
                      ))
    Users[0].addAccount(Account(id=len(Users[0].listAccount),
                                draft_qtd_limit=3,
                                draft_value_limit=500,
                                initial_value_account=0
                                ))
    Users[0].addAccount(Account(id=len(Users[0].listAccount),
                                draft_qtd_limit=3,
                                draft_value_limit=500,
                                initial_value_account=0
                                ))
    userMain(Users)
    
    



#regras de negócio

def checkIfNewDay(user:User = None, account : Account = None):
    global date
    now = DateController().registerMoment()
    if date.day!=now.day:
        date = DateController().registerMoment()
        


def login(Users : list):
    cpf = str(input("Informe o cpf: ").replace(".","").replace("-",""))
    index = findUserByCPF(Users,cpf)
    if index==-1:
        print("CPF não encontrado tente novamente")
        inp = str(input("1 - Tentar novamente\n2 - Voltar\n"))    
        if inp=='1' or inp=="Tentar novamente":
            return login(Users)
        else:
            return None
    else:
        return Users[index]
    
def findUserByCPF(Users : list, cpf : str) -> int:
    index = -1
    for user in Users:
        if user.cpf == cpf:
            print('\nLoggin realizado!\n\n')
            return index+1
        index+=1
    return -1

def createAccount(user : User):
    value = float(str(input("Qual o valor inicial depositado?\nR$")).replace(",","."))
    user.addAccount(Account(
        #por padrao
        id=len(user.listAccount),
        draft_qtd_limit=3,
        draft_value_limit=float(500),
        initial_value_account=value
    ))


def get_cep_request():
    try:
        cep_inp = str(input("0 - Voltar\nQual seu cep?\n")).replace("-","")
        if cep_inp == "0":
            return
        response  = requests.get(f'https://viacep.com.br/ws/{cep_inp}/json/')
        data = response.json()
        if response.status_code == 200:
            if len(data) <= 2:
                print("erro tente novamente!") 
                return get_cep_request()
            else:
                data["numero"] = str(input("Qual o numero da redência?"))
                print("endereco : " , data)
                return data
        else:
            print("erro tente novamente!") 
            return get_cep_request()   
    except:
        print("erro tente novamente!") 
        return get_cep_request()

def validar_cpf(cpf:str) -> bool:
    if len(cpf) != 11:
        return 0
    if cpf == cpf[0] * 11:
        return 0
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if digito1 != int(cpf[9]):
        return 0
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if digito2 != int(cpf[10]):
        return 0
    return 1


def createUser(Users: list):
    while True:
        cpf = str(input("Qual seu cpf?\n"))
        cpf = "".join(filter(str.isdigit, cpf))
        if validar_cpf(cpf):
            print("cpf aceito!")
            break
        else:
            if input("CPF inválido:\n1 - Tentar novamente\n2 - Voltar\n") == 2:
                return
    nome = str(input("Qual seu nome?\n"))
    nascimento = str(input("Qual a data de seu nascimento? em dd/mm/aaaa\n"))
    Users.append(User(cpf=cpf,
                      nome=nome,
                      data_nascimento=nascimento,
                      endereco= get_cep_request()
                      ))
    
def UserListAll(Users: list):
    for user in Users:
        print(f'CPF: {user.cpf}')
        print(f'Nome: {user.nome}')
        print(f'Data Nascimento: {user.data_nascimento}')
        print('Endereco: ')
        for item in user.endereco:
            print(f'    {item}:{user.endereco[item]}')
        print('Contas: ')
        aux = []
        for account in user.listAccount:
            aux.append([account.id,account.getAccountValue()])
        print(tabulate(aux,headers=["id","saldo"]))
    input('\nPress ENTER to continue')
if __name__ == "__main__":
    main()