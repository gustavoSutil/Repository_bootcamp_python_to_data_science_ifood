import requests
from classes.DateController import DateController
from classes.Account import Account
from classes.User import User
from tabulate import *


def checkIfNewDay(date,user:User = None, account : Account = None):
    now = DateController().registerMoment()
    if date.day!=now.day:
        date = DateController().registerMoment()
        #falta zerar os limites
        


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
    